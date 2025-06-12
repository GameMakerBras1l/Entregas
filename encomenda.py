from classes import Pacotes
from classes import Robos

produto = input("Informe o produto desejado: ")
peso = int(input("Informe o peso do produto: "))

pacote = Pacotes(produto, peso)


roboLeve = Robos("R1", 10)
roboLeve.entregar_pacote(pacote)

roboPesado = Robos("R2", 50)
roboPesado.entregar_pacote(pacote)
