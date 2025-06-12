#Passo 1: Criar classse para robo
#Passo 2: Criar Classe para pacote

class Robo:
    def __init__(self, id, capCargaKg):
        self.id = id
        self.capCargaKg = capCargaKg

    def realizarEntergas(self):
        if self.capCargakg >= Pacote.pesoKg:
            print("O ", self.id, " pode realizar a entrega.")
        else:
            print("O ", self.id, " não pode ser realizada.")

class Pacote:
    def __init__(self, conteudo, pesoKg, descricao, roboRespon):
        self.conteudo = conteudo
        self.pesoKg = pesoKg
        self.descricao = descricao
        self.roboRespon = roboRespon