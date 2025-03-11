class Tarefa:
    def __init__(self, task_id, titulo, descricao, status, prioridade, inicio, prazo):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.inicio = inicio
        self.prazo = prazo

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'prioridade': self.prioridade,
            'inicio': self.inicio,
            'prazo': self.prazo
        }
