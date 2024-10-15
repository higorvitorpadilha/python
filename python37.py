while True:
    numero_1 = int(input('Digite Um Numero: '))
    numero_2 = int (input ('Digie Outro Número: '))
    operador = input('Digite um operador(+-/*): ')

    if operador == '+':
     print (numero_1 + numero_2)
    if operador == '-':
     print(numero_1 - numero_2)
       
    if operador == '/':
     print(numero_1 / numero_2)
       
    if operador == '*':
     print(numero_1 * numero_2)
       
       
    sair= input('Quer [s]air: [s]im: ').lower().startswith('s')
    if sair is True:
     break