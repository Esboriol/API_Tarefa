from flask import Flask, request

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar JavaScript",
        "descricao": "Estudar um pouco sobre Django e como utilizalo eficientemente",
        "prioridade": "Urgente",
        "data_inicio": "25/02/2025",
        "prazo": "28/03/2025",
        "status": "Em andamento",
    },

    {
      "id": 2,
       "titulo": "Estudar Flask",
        "descricao": "Esturad Flask para aprender sobre Web Services",
        "prioridade": "Baixa Urgencia",
        "data_inicio": "25/02/2025",
        "prazo": "25/04/2025",
        "status": "Não iniciada"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa
    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    print(task)
    return ''

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_update = request.json
    task_search['titulo'] = task_update.get('titulo')
    task_search['descricao'] = task_update.get('descricao')
    task_search['status'] = task_update.get('status')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delet_task(task_id):

    # Procurar a tarefa com o task_id fornecido
    tarefa_a_deletar = None
    for tarefa in tarefas:
        if task_id == tarefa.get('id'):
            tarefa_a_deletar = tarefa
            break

    if tarefa_a_deletar:
        tarefas.remove(tarefa_a_deletar)
        return ''


if __name__ == '__main__':
    app.run(debug=True)