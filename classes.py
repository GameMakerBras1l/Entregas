# Passo 1: criar classes para robos e pacotes
# Passo 2: criar um sistema de entergas usando essas classes

class Robos:
    def __init__(self, idRobo, capKg):
        self.idRobo = idRobo
        self.capKg = capKg

    def entregar_pacote(self):
        if self.capKg >= 15:
            print("Entrega realizada")
        else:
            print("Entrega negada")