class personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    def atacar(self):
        print("personagem atacando")
    def subir_nivel(self):
        print("subiu de nivel")

class guerreiro(personagem):
    def atacar(self):
        print("atacando com espada")

class mago(personagem):
    def atacar(self):
        print("atacando com magia")

loloisa = mago("helo", 0)
loloisa.atacar()
loloisa.subir_nivel()

# class guerreiro(personagem):
#     def __init__(self):
#         super().__init__()
#         self.energia = 100
#     def __init__(self):
#         super().__init__()
#         self.nivel = 0
#     def atacar(self):
#         self.nivel = self.nivel + 10
#         self.energia = self.energia -10
#         print("O guerreiro atacou")

# class mago(personagem):
#     def __init__(self):
#         super().__init__()
#         self.energia = 100
#     def __init__(self):
#         super().__init__()
#         self.nivel = 0
#     def atacar(self):
#         self.nivel = self.nivel + 10
#         self.energia = self.energia - 20
#         print("o mago atacou")


# loloisa = mago()
# loloisa.atacar()
