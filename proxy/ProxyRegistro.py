# Loggin - Auditoria
from SistemaAtividade import SistemaAtividade
class ProxyRegistro:
    def __init__(self, usuario):
        self.sistema = SistemaAtividade()
        self.usuario = usuario

    def buscar_atividade(self, id):
        #conectar com o banco de Auditoria ou sistema de eventos (Kafka ou RabbitMQ)
        print(f"[LOG] {self.usuario} está buscando a atividade {id}")
        resultado = self.sistema.buscar_atividade(id)
        print(f"[LOG] atividade {id} encontrada.")
        return resultado
professor = ProxyRegistro("Joab")
professor.buscar_atividade(10)
