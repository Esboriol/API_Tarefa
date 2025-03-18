from venv import create

from database import get_db_connection

conexao = get_db_connection()

conexao.autocommit = True
cr = conexao.cursor()

create_table = """
    CREATE TABLE tarefas (
    task_id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    prioridade VARCHAR(20),
    data_inicio DATE,
    data_fim DATE,
    status VARCHAR(50)
    );
"""

# cr.execute(create_table)
print('Tabela criadas com sucesso')

registros = [
    (
        'Estudar Javascript',
        'Estudar Javascript para aprender web',
        'Alta',
        '2025-01-01',
        None,
        'Em andamento'
    ),
    (
        'Sair do celular',
        'Sair do celular para aprender programacao',
        'Alta',
        '2025-03-18',
        None,
        'Em andamento'
    )
]

insert = """
    INSERT INTO tarefas (titulo, descricao, prioridade, data_inicio, data_fim, status) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""

# cr.executemany(insert, registros)
print('Registros inseridos com sucesso')

cr.close()
conexao.close()
