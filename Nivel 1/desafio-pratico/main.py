
def adicionar_contato(nome_contato, numero_contato, lista_contatos):
    contato = {"nome": nome_contato, "numero": numero_contato, "isFavorite": False}
    lista_contatos.append(contato)
    print("Contato adicionada com sucesso!")

def listar_contatos(lista_contatos):
    if not lista_contatos:
        print("Nenhuma contato cadastrado!")
    else:
        print("\n\tContatos: ")    
        for index, contato in enumerate(lista_contatos):
            isFavorite = contato["isFavorite"]
            if isFavorite: 
                print(f"\n{index} - ⭐ {contato['nome']} - {contato['numero']}")
            else:
                print(f"\n{index} - {contato['nome']} - {contato['numero']}")

def favoritar_contato(index, lista_contatos):   
    if not lista_contatos:
        return
    lista_contatos[index]["isFavorite"] = True
    print("\nContato marcada como favorito!")

def editar_contato():
    contatos_favoritos.clear()
    print("\nContatos favoritos removidas com sucesso!")

contatos = []
while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Favoritar Contato")
    print("4. Editar contato")
    print("5. Sair")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        nome_contato = input("\nDigite o nome do contato: ")
        numero_contato = input("\nDigite o número do contato: ")
        adicionar_contato(nome_contato, numero_contato, contatos)
    elif escolha == "2":
        listar_contatos(lista_contatos=contatos)
    elif escolha == "3":
        if not contatos:
            print("Nenhum contato cadastrado!")
            continue

        for index, contato in enumerate(contatos):
            if(not contato["isFavorite"]):
                print(f"{index} - {contato['nome']} - {contato['numero']}")

        index_contato = int(input("\nQual contato deseja favoritar? "))
        favoritar_contato(index_contato, contatos)
    elif escolha == "4":
        editar_contato()
    elif escolha == "5":
        print("\nAté mais :)\n")
        break
    else:
        print("Opção inválida. Tente novamente.")