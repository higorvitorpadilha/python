lista = ['Arroz', 'Feijão', 'Macarrão', 'miojo']

while True:
    adicionar = input("Você quer inserir um item na sua lista? [S]IM ou [N]ÃO: ").lower()
    
    if adicionar == 's':
        item_adicionado = input("Qual item você quer adicionar? ")
        lista.append(item_adicionado)
        print("Lista atual:", lista)
    elif adicionar == 'n':
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

while True:
    apagar = input("Você quer apagar algo? [S]im ou [N]ão: ").lower()
    
    if apagar == 's':
        print("\nLista com índices:")
        for i, item in enumerate(lista):
            print(f"{i}: {item}")
        
        try:
            indice_para_remover = int(input("\nDigite o índice do item que você quer apagar: "))
            if 0 <= indice_para_remover < len(lista):
                item_removido = lista.pop(indice_para_remover)
                print(f"Item '{item_removido}' removido com sucesso!")
                print("Lista atualizada:", lista)
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
    elif apagar == 'n':
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

listar = input("Você quer listar sua lista? [S]im ou [N]ão: ").lower()
if listar == 's':
    print("Lista final:", lista)
