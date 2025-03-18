class Tarefa:

    def __init__(self, task_id, titulo, descricao, status,
                 prioridade, data_inicio, data_fim):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def to_json(self):
        return {
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }