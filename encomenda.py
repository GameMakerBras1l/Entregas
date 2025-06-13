from classes import Pacotes
from classes import Robos

produto = input("Informe o produto desejado: ")
peso = int(input("Informe o peso do produto: "))

pacote = Pacotes(produto, peso)
if peso <= 10:
    roboLeve = Robos("R1", 10)
    roboLeve.entregar_pacote(pacote)
elif 10 < peso <= 50:
    roboPesado = Robos("R2", 50)
    roboPesado.entregar_pacote(pacote)
else:
    print("Excesso de peso, falha no encaminhamento do produto")
