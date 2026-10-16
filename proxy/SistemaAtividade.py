class SistemaAtividade: 
    def __init__(self):
        print("Criando o sistema de atividades.")

    def buscar_atividade(self,id):
        return f"Atividade {id} encontrada."

    def enviar_atividade(self, id, resposta):
        print(f"Enviando atividade {id}")
        print(f"Resposta recebida: {resposta}")
        return "Atividade enviada com sucesso."

    def atribuir_nota(self, id, nota):
        print(f"atribuindo nota")
        print(f"Nota: {nota}")
        return "Nota atribuida com sucesso."