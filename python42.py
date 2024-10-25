palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:
    tentativas += 1
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palvra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palvra_formada += letra_secreta
        else:
            palvra_formada +='*'

    print('Palvra formada', palvra_formada)

    if palvra_formada == palavra_secreta:
        print('Parabens você acertou')
        print('A palavra era', palvra_formada)
        print('As tentativas foram', tentativas)
       
   
