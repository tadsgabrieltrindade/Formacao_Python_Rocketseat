
tarefas = []
tarefas_concluidas = []


def adicionar_tarefa():
    tarefa = input("\nQual é a tarefa? ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas and not tarefas_concluidas:
        print("Nenhuma tarefa cadastrada!")
    else:
        print("\n\tTarefas em aberto")    
        for index, tarefa in enumerate(tarefas):
            print(f"\n[ ] - {index} - {tarefa}")

        print("\n\n\tTarefas concluídas")
        
        for index2, elemento2 in enumerate(tarefas_concluidas):
            print(f"\n[X] - {index2} - {elemento2}")

def concluir_tarefa():
    if not tarefas and not tarefas_concluidas:
        print("\nNenhuma tarefa pendente!")
        return
    
    for index, elemento in enumerate(tarefas):
        print(f"\n{index} - {elemento}")
    opc = int(input("\nQual tarefa deseja concluir?"))

    tarefas_concluidas.append(tarefas[opc])
    tarefas.pop(opc)
    print("\nTarefa marcada como concluída!")

def remover_tarefas_concluidas():
    tarefas_concluidas.clear()
    print("\nTarefas concluídas removidas com sucesso!")


while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluír Tarefa")
    print("4. Remover tarefas concluídas")
    print("5. Sair")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        concluir_tarefa()
    elif escolha == "4":
        remover_tarefas_concluidas()
    elif escolha == "5":
        print("\nAté mais :)\n")
        break
    else:
        print("Opção inválida. Tente novamente.")