# Passo 1: Criar classe robo

class Robo:
    # Construtor da classe
    def __init__(self, id, capCargaKg):
        self.id = id
        self.capCargaKg = capCargaKg



RoboLeve = Robo(str("RB-01"), int(10))

RoboPesado = Robo(str("RB-02"), int(50))