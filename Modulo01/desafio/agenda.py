# Desafio do Módulo: Introdução ao Python


def adicionar_contato(contatos, nome, telefone, email, favorito=False):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }

    contatos.append(contato)
    print(f"\nContato {nome} adicionado com sucesso")
    return


def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for index, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "♥" if contato["favorito"] else " "
        print(
            f"{index}. [{favorito}] {nome} - {telefone} - {email}")
    return


def atualizar_contato(contatos, index, nome, telefone, email):
    contatos[index]["nome"] = nome
    contatos[index]["telefone"] = telefone
    contatos[index]["email"] = email
    print("\nContato atualizado com sucesso!")
    return


def marcar_desmarcar_favorito(contatos, index):
    contatos[index]["favorito"] = not contatos[index]["favorito"]
    favorito = "♥" if contatos[index]["favorito"] else " "
    print(
        f"\nContato {contatos[index]['nome']} marcado como favorito {favorito}")
    return


def ver_favoritos(contatos):
    print("\nLista de Favoritos:")
    for index, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(
                f"{index}. {nome} - {telefone} - {email}")
    return


def deletar_contato(contatos, index):
    contatos.pop(index)
    print("\nContato deletado com sucesso!")
    return


contatos = []

while True:
    print("\nMenu da Agenda")
    opcoes = ["Adicionar contato", "Ver contatos",
              "Atualizar contato", "Marcar/Desmarcar Favorito", "Ver Favoritos", "Deletar contato", "Sair"]

    for index, opcao in enumerate(opcoes, start=1):
        print(f"{index}. {opcao}")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        print("\nAdicionar Contato")
        nome = input("\nNome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        index = int(
            input("\nDigite o número do contato que deseja atualizar: ")) - 1
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        atualizar_contato(contatos, index, nome, telefone, email)
    elif escolha == "4":
        ver_contatos(contatos)
        index = int(
            input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
        marcar_desmarcar_favorito(contatos, index)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        index = int(
            input("\nDigite o número do contato que deseja deletar: ")) - 1
        deletar_contato(contatos, index)
    elif escolha == "7":
        break
    else:
        print("\nOpção Inválida")
        continue

print("\nPrograma Finalizado")
