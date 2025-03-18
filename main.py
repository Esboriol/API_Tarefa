from flask import Flask, request
from tarefa_controller import get_tarefas, get_tarefa, criar_tarefa, remover_tarefa, atualizar_task

app = Flask(__name__)

tarefas = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return get_tarefas()

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    return get_tarefa(task_id)

@app.route('/tasks', methods=['POST'])
def create_task():
    return criar_tarefa(request.json)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return atualizar_task

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return remover_tarefa(task_id)

if __name__ == '__main__':
    app.run(debug=True)
