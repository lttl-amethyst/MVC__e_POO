from SistemaAtividade import SistemaAtividade
class AtribuirNota:
    def __init__(self, usuario):
        self.sistema = SistemaAtividade()
        self.usuario = usuario

    def atribuir_nota(self, id, nota):
        if self.usuario != "professor":
            print("Acesso permitido apenas para professores.")
            return None
        return self.sistema.atribuir_nota(id, nota)

professor = AtribuirNota("professor")
aluno = AtribuirNota("aluno")
professor.atribuir_nota(10, "9")
aluno.atribuir_nota(10, "10")
        
