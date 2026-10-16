# Controle de Acesso
from SistemaAtividade import SistemaAtividade
class ProxyProtecao:
    def __init__(self, usuario):
        self.sistema = SistemaAtividade()
        self.usuario = usuario #aluno ou professor

    def enviar_atividade(self, id, resposta):
        if self.usuario != "aluno":
            print("Acesso permitido apenas para alunos.")
            return None # retorna nada
        return self.sistema.enviar_atividade(id, resposta)
    
professor = ProxyProtecao("professor")
aluno = ProxyProtecao("aluno")
professor.enviar_atividade(10, "Cristovão Colombo")
aluno.enviar_atividade(10, "Cristovão Colombo")

        