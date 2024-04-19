def adicionar_tarefa(tarefas, nome_tarefa="tarefa padrão"):
    # tarefa : nome da tarefa
    # completada: indica se a tarefa está completada
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)

    print(f"\nTarefa '{nome_tarefa}' adicionada com sucesso!")
    return


tarefas = []


while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    opcoes = ["Adicionar tarefa", "Ver tarefas",
              "Atualizar Tarefa", "Completar Tarefa", "Deletar tarefas completadas", "Sair"]

    for index, opcao in enumerate(opcoes):
        print(f"{index + 1}. {opcao}")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("\nDigite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "6":
        break

print("\nPrograma finalizado")
