cpf_enviado_usuario = '18011239007'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1+=int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 *10) %11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 +=int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 =(resultado_digito_2 *10) %11  
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)  

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == novo_cpf:
    print(f'{cpf_enviado_usuario}  é valido')
else:
    print('CPF invalido')