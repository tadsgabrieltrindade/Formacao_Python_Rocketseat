
def imprimir_contato(index, lista_contatos):
    print(f"\n1 - Nome: {lista_contatos[index]['nome']}")
    print(f"2 - Número: {lista_contatos[index]['numero']}")
    print(f"3 - E-mail: {lista_contatos[index]['email']}")
    print(f"4 - Favorito: {'Sim ⭐' if lista_contatos[index]['isFavorite'] else 'Não'}")

def imprimir_contatos(lista_contatos, so_favoritos = False):
    print("\n\tContatos: ") 
    for index, contato in enumerate(lista_contatos):
        isFavorite = contato["isFavorite"]
        if isFavorite: 
            print(f"\n{index} - {contato['nome']} - {contato['email']} - {contato['numero']} ⭐ ")
        else:
            if not so_favoritos:
                print(f"\n{index} - {contato['nome']} - {contato['email']} - {contato['numero']}")

def adicionar_contato(nome_contato, numero_contato, email_contato, lista_contatos):
    contato = {"nome": nome_contato, "numero": numero_contato, "email": email_contato, "isFavorite": False}
    lista_contatos.append(contato)
    print("Contato adicionada com sucesso!")

def listar_contatos(lista_contatos):
    if not lista_contatos:
        print("Nenhuma contato cadastrado!")
    else:
        imprimir_contatos(lista_contatos)

def favoritar_contato(index, lista_contatos):   
    if not lista_contatos:
        return
    lista_contatos[index]["isFavorite"] = True
    print("\nContato marcada como favorito!")

def editar_contato(index, lista_contatos):  
    if not lista_contatos:
        return    
    #solicitar qual dado ele quer alterar
    imprimir_contato(index, lista_contatos)
    print(f"5 - voltar")
    escolha = input("\nQual dado você deseja alterar? ")

    #a cada escolha, fazer seu switch
    if escolha == "1" or escolha == "2" or escolha == "3":
        novo_valor = input("\nQual é o novo valor para ele? ")
        if escolha == "1":
            lista_contatos[index]['nome'] = novo_valor
        elif escolha == "2":
            lista_contatos[index]['numero'] = novo_valor
        elif escolha == "3":
            lista_contatos[index]['email'] = novo_valor
        print("\nContato alterado com sucesso")    
    elif escolha == "4": 
        if lista_contatos[index]['isFavorite']:
            lista_contatos[index]['isFavorite'] = False
            print("\nContato desfavoritado!")
        else: 
            lista_contatos[index]['isFavorite'] = True
            print("\nContato favoritado!")
    elif escolha == "5":
        return
    imprimir_contato(index, lista_contatos)
    return

def apagar_contato(index, lista_contatos):
    lista_contatos.pop(index_contato)
    print("\nContato excluído com sucesso!")

contatos = []
while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Favoritar Contato")
    print("4. Editar contato")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("0. Sair")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        nome_contato = input("\nDigite o nome do contato: ")
        numero_contato = input("\nDigite o número do contato: ")
        email_contato = input("\nDigite o e-mail do contato: ")
        adicionar_contato(nome_contato, numero_contato, email_contato, contatos)

    elif escolha == "2":
        listar_contatos(lista_contatos=contatos)

    elif escolha == "3" or escolha == "4" or escolha == "6":
        if not contatos:
            print("Nenhum contato cadastrado!")
            continue

        imprimir_contatos(contatos)

        index_contato = int(input("\nQual contato deseja? "))
        if escolha == "3":
            favoritar_contato(index_contato, contatos)
        elif escolha == "4":
            editar_contato(index_contato, contatos)
        elif escolha == "6":
            apagar_contato(index_contato, contatos)
    
    elif escolha == "5":
        if not contatos:
            print("Nenhum contato cadastrado!")
            continue
        imprimir_contatos(contatos, True)

    elif escolha == "0":
        print("\nAté mais :)\n")
        break

    else:
        print("Opção inválida. Tente novamente.")