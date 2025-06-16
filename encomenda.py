from classes import Pacotes, Robos, RegistroEntregas

lista_pacotes = [
    Pacotes(1, "Livro", 2, 1),
    Pacotes(2, "Figure", 4, 1),
    Pacotes(3, "Camisa", 0.5, 1),
    Pacotes(4, "Jogo", 0.5, 1)
]

registro = RegistroEntregas()

while True:
    print("\nProdutos disponíveis:")
    for p in lista_pacotes:
        print(f"ID: {p.idProduto} | Nome: {p.conteudo} | Peso (kg): {p.pesoKg}")

    escolha = input("Digite o ID do produto (ou 'S' para sair): ")
    if escolha.lower() == 's':
        break

    if not escolha.isdigit():
        print("ID inválido, tente novamente.")
        continue

    idPacote = int(escolha)
    pacote = next((p for p in lista_pacotes if p.idProduto == idPacote), None)
    if pacote is None:
        print("Produto não encontrado, tente de novo.")
        continue

    qtd_input = input(f"Quantidade de '{pacote.conteudo}': ")
    if not qtd_input.isdigit() or int(qtd_input) < 0:
        print("Quantidade inválida.")
        continue

    qtd = int(qtd_input)
    pacote.atualizar_quantidade(qtd)
    peso = pacote.pesoTotal
    print(f"Peso total do pacote: {peso} kg")

    if peso <= 10:
        robo = Robos("RB-01", 10)
        registro.registrar(robo, pacote)
    elif peso <= 50:
        robo = Robos("RB-02", 50)
        registro.registrar(robo, pacote)
    else:
        print("Excesso de peso — entrega falhou.")

print("Resumo das entregas:")
registro.resumo()