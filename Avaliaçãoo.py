def cadastrar_produto(produtos, nome, valor, quantidade, imp1, imp2, imp3, frete, lucro):
    produto = {
        'Nome': nome,
        'Valor': valor,
        'Quantidade': quantidade,
        'Imposto1': imp1,
        'Imposto2': imp2,
        'Imposto3': imp3,
        'Frete': frete,
        'Lucro': lucro
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    print("_____________________")
    print("\n")

def imprimir_produtos(produtos):
    for indice, produto in enumerate(produtos):
        print(f"ID do produto {indice}")
        print(f"Produto: {produto['Nome']} ")
        print(f"Valor: {produto['Valor']} R$")
        print(f"Quantidade: {produto['Quantidade']} ")
        print(f"Primeiro imposto: {produto['Imposto1']} R$ ")
        print(f"Segundo imposto: {produto['Imposto2']} R$ ")
        print(f"Terceiro imposto: {produto['Imposto3']} R$ ")
        print(f"Valor do frete: {produto['Frete']}")
        print(f"Lucro: {produto['Lucro']}")
        print("_____________________")
        print("\n")

def atualizar_produtos(produtos, nome, valor, quantidade, imp1, imp2, imp3, frete, lucro, indice):
    if 0 <= indice < len(produtos):
        produtos[indice]['Nome'] = nome
        produtos[indice]['Valor'] = valor
        produtos[indice]['Quantidade'] = quantidade
        produtos[indice]['Imposto1'] = imp1
        produtos[indice]['Imposto2'] = imp2
        produtos[indice]['Imposto3'] = imp3
        produtos[indice]['Frete'] = frete
        produtos[indice]['Lucro'] = lucro
        print("Produto editado com sucesso!")
    else:
        print("Índice inválido. Produto não encontrado.")

def excluir_produto(produtos, indice):
    if 0 <= indice < len(produtos):
        del produtos[indice]
        print("Produto deletado com sucesso!")
        print("_____________________")
        print("\n")
    else:
        print("Índice inválido. Produto não encontrado.")

def mudar_quantidade(produtos, indice):
    if 0 <= indice < len(produtos):
        print(f"Nome do produto: {produtos[indice]['Nome']}")
        print(f"Quantidade: {produtos[indice]['Quantidade']}")

        a = input("Se quiser ADCIONAR: 1\nSe quiser SUBTRAIR: 2\nDigite o número da ação desejada: ")

        if a == '1':
            produtos[indice]['Quantidade'] += int(input("Digite a quantidade que deseja acrescentar: "))
        elif a == '2':
            produtos[indice]['Quantidade'] -= int(input("Digite a quantidade que deseja diminuir: "))
        print("Quantidade atualizada com sucesso!")
        print("____________________")
        print("\n")
    else:
        print("Produto não encontrado")

produtos = []
while True:

    print("\nMenu:")
    print("Cadastrar um produto: 1")
    print("Imprimir produtos cadastrados: 2 ")
    print("Editar produtos: 3")
    print("Mudar quantidade de produtos: 4")
    print("Deletar produto cadastrado: 5")
    print("Fechar programa: 6")
    a = input("Digite o número da ação desejada: ")

    if a == "1":
        nome = input("Digite o produto que deseja cadastrar: ")
        valor = float(input("Valor da unidade do produto: "))
        quantidade = int(input("Quantidade de unidades desse produto: "))
        frete = float(input("Valor do frete desse produto: "))
        imposto1 = float(input("Valor do primeiro imposto: "))
        imposto2 = float(input("Valor do segundo imposto: "))
        imposto3 = float(input("Valor do terceiro imposto: "))
        lucro = float(input("Margem de lucro"))

        imposto1 = (valor * imposto1) / 100
        imposto2 = (valor * imposto2) / 100
        imposto3 = (valor * imposto3) / 100
        frete = frete / quantidade
        preço_final = valor + imposto1 + imposto2 + imposto3 + frete
        venda = preço_final + (preço_final * (lucro / 100))
        cadastrar_produto(produtos, nome, valor, quantidade, imposto1, imposto2, imposto3, frete, lucro)

    elif a == "2":
        imprimir_produtos(produtos)

    elif a == "3":
        indice = int(input("Digite o ID do produto que deseja editar: "))
        atualizar_produtos(produtos, nome, valor, quantidade, imposto1, imposto2, imposto3, frete, lucro, indice)

    elif a == "4":
        indice = int(input("Digite o ID do produto que deseja editar: "))
        mudar_quantidade(produtos, indice)

    elif a == "5":
        indice = int(input("Digite o ID do produto que deseja excluir: "))
        excluir_produto(produtos, indice)

    elif a == "6":
        print("Encerrando programa")
        break

    else:
        print("Ação não encontrada")