def cadastrar_cliente(clientes,nome,email,telefone):
    cliente={
        'Nome' : nome,
        'Email' :email,
        'Telefone' :telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado!")
    print("****************************")
    print("\n")

def imprimir_cliente(clientes):
    for indice,cliente in enumerate(clientes):
        print(f"ID cliente {indice}")
        print(f"Nome: {cliente['Nome']}")
        print(f"Email: {cliente['Email']}")
        print(f"Telefone: {cliente['Telefone']}")
        print("****************************")
        print("\n")

def atualizar_cliente(nome,email,telefone,indice):
    if 0 <= indice < len(clientes) :
        clientes[indice]['Nome'] = nome
        clientes[indice]['Email'] = email
        clientes[indice]['Telefone'] = telefone

        print("Cliente editado com sucesso!")
        print("****************************")
        print("\n")
    else:
        print("Indice invalido. Cliente não encontrado.")

def deletar_cliente(cliente,indice) :
    if 0 <= indice < len(clientes) :
        del clientes[indice]
        print("Cliente deletado com sucesso!")
        print("****************************")
        print("\n")

clientes = []

while True :
    print("Menu :")
    print("Cadastrar um cliente: 1")
    print("Imprimir clientes cadastrados digite: 2 ")
    print("Editar clientes já cadastrados digite: 3")
    print("Excluir cadastro digite: 4")
    print("Fechar programa digite: 5")
    
    a=str(input("Digite o numero da ação desejada: "))

    if a == "1" :
        nome=str(input("Digite o seu nome: "))
        email=str(input("Digite o seu email: "))
        telefone=str(input("Digite o seu numero: "))
        cadastrar_cliente(clientes,nome,email,telefone)

    elif a == "2" :
        imprimir_cliente(clientes)

    elif a == "3" :
        indice=int(input("Digite o seu ID para editar: "))
        nome=str(input("Digite o seu novo nome: "))
        email=str(input("Digite o seu novo email: "))
        telefone=str(input("Digite o seu novo numero: "))
        atualizar_cliente(nome,email,telefone,indice)

    elif a == "4" :
        indice=int(input("Digite o seu ID para apagar: "))
        deletar_cliente(clientes,indice)

    elif a == "5" :
        print("Encerrando programa")
        break

    else :
        print("Esta ação não existe")