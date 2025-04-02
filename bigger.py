#funcao maior numero
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

def maiorNumero(a, b):
    if a > b:
        print(f"O numero {a} é maior do que {b}")
    elif a == b:
        print(f"O numero {a} é igual a {b}")
    else:
        print(f"O numero {b} é maior do que {a}")

maiorNumero(a,b)