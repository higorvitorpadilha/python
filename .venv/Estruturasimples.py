a= input("Informe um valor par aa variavel a: ")
b= input("Informe um valor par aa variavel b: ")

if (a>b):
    aux = a;
    a=b;
    b=aux;

print("O valor da variavel agora a é: ", a)
print("O valor da variavel agora b é: ", b)