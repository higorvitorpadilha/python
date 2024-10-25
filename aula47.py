import os 

lista = []

while True:
        print('Selecioneuma opção')
        opção= input('[i]nserir, [a]pagar, [l]istar: ').lower()

        if opção == 'i':
            os.system('cls')
            valo = input('valor: ')
            lista.append(valo)
        elif opção == 'a':
            indice_str = input('Digite o indice que você quer apagar: ')

            try:
                  indice = int(indice_str)
                  del lista [indice]
            except ValueError:
                    print('indice não existe na lista.')
            except Exception:
                  print('erro desconhecido')
                  

        elif opção == 'l':
              os.system('cls')
              for i,valor in enumerate(lista):
                    print(i,valor)
        else:
              print('Você colocou um valor inexistente, assim o programa foi finalizado')
              break
