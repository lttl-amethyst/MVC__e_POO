class Email:
    def __init__(self, dest, assunto, corpo, assinatura):
        self.dest = dest
        self.assunto = assunto 
        self.corpo = corpo
        self.assinatura = assinatura

    def __str__(self):
        return(f"Para: {self.dest}\n"
               f"Assunto: {self.assunto}\n"
               f"Mensagem: {self.corpo}\n"
               f"At.te\n"
               f"---\n"
               f"{self.assinatura}")
    
class EmailBuilder:
    def __init__(self):
        self.dest = ""
        self.assunto = ""
        self.corpo = ""
        self.assinatura = ""
    def para(self, dest):
        self.dest = dest
        return self
    def com_assunto(self, assunto):
        self.assunto = assunto
        return self
    def com_corpo(self, corpo):
        self.corpo = corpo
        return self
    def com_assinatura(self, assinatura):
        self.assinatura = assinatura
        return self

    def build(self):
        return Email(
            self.dest,
            self.assunto,
            self.corpo,
            self.assinatura
        )

boas_vindas = (EmailBuilder()
                .para("Todos")
                .com_corpo("Bem-vindos")
                .com_assinatura("helo")
                .build())
print(boas_vindas)

churrasco = (EmailBuilder()
                .para("Amigos")
                .com_assunto("Churras")
                .com_corpo("Churras sábado 11h")
                .build())
print(churrasco)