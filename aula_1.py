class RPG:
    def __init__(self, cartas, tabuleiro, historia):
        self.cartas = cartas
        self.tabuleiro = tabuleiro
        self.historia = historia
    def regenerar(self):
        print("o personagem regenerou")
    def atacar(self):
        print("o personagem atacou")
    def avançar(self):
        print("o personagem avançou")

RPG_do_pedro = RPG(["atacar"], ["regenerar"], ["defender"], "Ouija", "Aventura")