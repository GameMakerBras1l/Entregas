from classes import Pacotes
from classes import Robos

lista_pacotes = [
    Pacotes(1, "Livro", 2, 1),
    Pacotes(2, "Figure", 4, 1),
    Pacotes(3, "Camisa", 0.5, 1),
    Pacotes(4, "Jogo", 0.5, 1)
]

print("Produtos disponíveis: ")
for p in lista_pacotes:
    print("ID: ", p.idProduto, " | Nome: ", p.conteudo, " | Peso Liquido: ", p.pesoKg, "Kg")

idPacote = int(input("Digite o ID do produto: "))
pacotEscolhido = next((p for p in lista_pacotes if p.idProduto == idPacote), None)

if pacotEscolhido:
    qtd = int(input(f"Digite a quantidade de '{pacotEscolhido.conteudo}' desejada: "))
    pacotEscolhido.atualizar_quantidade(qtd)
    pesoEntrega = pacotEscolhido.pesoTotal

    print(f"\nProduto selecionado: {pacotEscolhido.conteudo}")
    print(f"Quantidade: {qtd}")
    print(f"Peso total: {pesoEntrega}kg")

    # Seleção do robô com base no peso
    if pesoEntrega <= 10:
        robo = Robos("RB-01", 10)
        robo.entregar_pacote(pacotEscolhido)
    elif 10 < pesoEntrega <= 50:
        robo = Robos("RB-02", 50)
        robo.entregar_pacote(pacotEscolhido)
    else:
        print("Excesso de peso, falha no encaminhamento do produto.")
else:
    print("Produto com esse ID não encontrado.")