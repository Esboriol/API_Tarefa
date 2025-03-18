from database import get_db_connection
from tarefa import Tarefa

def get_tarefas():
    conexao = get_db_connection()
    cr = conexao.cursor()

    cr.execute(
        """
        SELECT 
            task_id, titulo, descricao, prioridade, 
            to_char(data_inicio, 'DD/MM/YYYY') as data_inicio,
            to_char(data_fim, 'DD/MM/YYYY') as data_fim,
            status
        FROM
            tarefas;
        """
    )

    resultados = cr.fetchall()

    cr.close()
    conexao.close()

    tarefas = []

    for resultado in resultados:
        tarefa = Tarefa(task_id=resultado[0],
                        titulo=resultado[1],
                        descricao=resultado[2],
                        prioridade=resultado[3],
                        data_inicio=resultado[4],
                        data_fim=resultado[5],
                        status=resultado[6])
        tarefas.append(tarefa.to_json())

    return tarefas

def get_tarefa(tarefa_id):
    conexao = get_db_connection()
    cr = conexao.cursor()

    cr.execute(
        """
        SELECT
            task_id, titulo, descricao, prioridade,
            to_char(data_inicio, 'DD/MM/YYYY') as data_inicio,
            to_char(data_fim, 'DD/MM/YYYY') as data_fim,
            status
        FROM
            tarefas
        WHERE
            task_id = %s    
        """, (tarefa_id,)
    )

    resultado = cr.fetchone()

    cr.close()
    conexao.close()

    tarefa = Tarefa(task_id=resultado[0],
                    titulo=resultado[1],
                    descricao=resultado[2],
                    prioridade=resultado[3],
                    data_inicio=resultado[4],
                    data_fim=resultado[5],
                    status=resultado[6])

    return tarefa.to_json()

def criar_tarefa(dados):
    conexao = get_db_connection()
    cr = conexao.cursor()

    cr.execute(
        """
            INSERT INTO tarefas (titulo, descricao, prioridade, data_inicio, data_fim, status)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING task_id;
        """,
              (dados.get('titulo'), dados.get('descricao'),
              dados.get('prioridade'), dados.get('data_inicio'),
              dados.get('data_fim'), dados.get('status')
            )
    )

    tarefa_id_inserido = cr.fetchone()[0]

    conexao.commit()
    cr.close()
    conexao.close()

    tarefa = get_tarefa(tarefa_id_inserido)

    return tarefa

def remover_tarefa(task_id):
    conexao = get_db_connection()
    cr = conexao.cursor()

    cr.execute(
        """
        DELETE FROM tarefas WHERE task_id = %s
        """, (task_id,)
    )

    conexao.commit()
    cr.close()
    conexao.close()

    return 'Tarefa removida com sucesso'

def atualizar_task(task_id, dados):
    conexao = get_db_connection()
    cr = conexao.cursor()

    cr.execute(
        """
        UPDATE tarefas
            SET status = %s
        WHERE
            task_id = %s
        RETURNING status
        """, (dados.get('status'), task_id)
    )
    resultados = cr.execute()
    conexao.commit()
    cr.close()
    conexao.close()

    if resultados:
        tarefa = Tarefa(task_id=resultados[0], titulo=[1], descricao=[2], prioridade=resultados[3],
                        data_inicio=resultados[4], data_fim=resultados[5], status=[6])
        return tarefa.to_json()
    else:
        return None