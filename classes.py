# Passo 1: criar classes para robos e pacotes
# Passo 2: criar um sistema de entergas usando essas classes

class Pacotes:
    def __init__(self, conteudo, pesoKg):
        self.conteudo = conteudo
        self.pesoKg = pesoKg

class Robos:
    def __init__(self, idRobo, capKg):
        self.idRobo = idRobo
        self.capKg = capKg

    def entregar_pacote(self, pacote):
        if self.capKg >= pacote.pesoKg:
            print("Entrega encaminhada")