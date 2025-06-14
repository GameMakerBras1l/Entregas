from classes import Pacotes
from classes import Robos



produto = input("Informe o produto desejado: ")
peso = int(input("Informe o peso do produto: "))
numero = int(input("Informe a quaantidade desse produto: "))



pacote = Pacotes(produto, peso, numero)
pesoEntrega = pacote.pesoTotal

if pesoEntrega <= 10:
    roboLeve = Robos("R1", 10)
    roboLeve.entregar_pacote(pacote)

elif 10 < pesoEntrega <= 50:
    roboPesado = Robos("R2", 50)
    roboPesado.entregar_pacote(pacote)

else:
    print("Excesso de peso, falha no encaminhamento do produto")
