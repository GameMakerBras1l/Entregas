# Passo 1: criar classes para robos e pacotes
# Passo 2: criar um sistema de entergas usando essas classes

class Pacotes:
    def __init__(self, conteudo, pesoKg, numProdutos):
        self.conteudo = conteudo
        self.pesoKg = pesoKg
        self.numProdutos = numProdutos
        self.pesoTotal = self.numProdutos * self.pesoKg

    def num_produtos(self):
        return self.pesoTotal

class Robos:
    def __init__(self, idRobo, capKg):
        self.idRobo = idRobo
        self.capKg = capKg
        self.falhaEntre = 0
        self.sucessoEntre = 0

    def entregar_pacote(self, pacote):
        if self.capKg >= pacote.pesoTotal:
            print("Entrega encaminhada")

            self.sucessoEntre += 1
        else:
            self.falhaEntre += 1