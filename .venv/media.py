notaa= float (input("Informe a primeira nota: "))
notab= float (input("Digite a segunda nota: "))

media_final= (notaa + notab) / 2


if media_final >= 7:
    print("A sua média foi: ", media_final, "você está Aprovado")

elif media_final >= 6:
    print("Recuperação")

else:
    print("A sua média foi: ", media_final, "Você foi REPROVADO")