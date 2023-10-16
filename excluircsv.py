def excluir_pessoa(pessoas, email):
    pessoa_registrada = None
    for pessoa in pessoas:
        if pessoa['Email'] == email:
            pessoa_registrada = pessoa
            break
    if pessoa_registrada:
        pessoas.delete(pessoa_registrada)
        print(f"A pessoa com o email {email} foi excluída.")
    else:
        print("Esta pessoa não esta registrada")