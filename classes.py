# Passo 1: criar classes para robos e pacotes
# Passo 2: criar um sistema de entergas usando essas classes

class Pacotes:
    def __init__(self, idProtduto, conteudo, pesoKg, numProdutos):
        self.idProduto = idProtduto
        self.conteudo = conteudo
        self.pesoKg = pesoKg
        self.numProdutos = numProdutos
        self.pesoTotal = self.numProdutos * self.pesoKg

    def atualizar_quantidade(self, nova_qtd):
        self.numProdutos = nova_qtd
        self.pesoTotal = self.numProdutos * self.pesoKg
        return self.pesoTotal

class Robos:
    def __init__(self, idRobo, capKg):
        self.idRobo = idRobo
        self.capKg = capKg
        

    def entregar_pacote(self, pacote):
        if self.capKg >= pacote.pesoTotal:
            print("Entrega encaminhada")
            status = "Sucesso"

        else:
            print("Falha no encaminhamento")
            status = "Falha"
        
        return status
    
class RegistroEntregas:
    def __init__(self):
        self.registros = {}

    def registrar(self, robo, pacote):
        status = robo.entregar_pacote(pacote)

        if robo.idRobo not in self.registros:
            self.registros[robo.idRobo] = {'sucesso': 0, 'falha': 0}

        self.registros[robo.idRobo][status.lower()] += 1
        return status

    def obter_status(self, idRobo):
        return self.registros.get(idRobo, {'sucesso': 0, 'falha': 0})

    def resumo(self):
        for idRobo, stats in self.registros.items():
            print(f"Robo {idRobo}: {stats['sucesso']} sucesso(s), {stats['falha']} falha(s)")
