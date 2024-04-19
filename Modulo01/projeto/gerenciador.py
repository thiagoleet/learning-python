while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    opcoes = ["Adicionar tarefa", "Ver tarefas",
              "Atualizar Tarefa", "Completar Tarefa", "Deletar tarefas completadas", "Sair"]

    for index, opcao in enumerate(opcoes):
        print(f"{index + 1}. {opcao}")

    escolha = input("\nDigite a sua escolha:")

    if escolha == "6":
        break
