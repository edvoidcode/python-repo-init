# Crie um programa que permita somar, subtrair, multiplicar e dividir dois números.

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação que deseja realizar (+,-,* ou /): ")

if operacao == "+":
    resultado = a+b
elif operacao == "-":
    resultado = a-b
elif operacao == "*":
    resultado = a*b
elif operacao == "/":
    resultado = a/b
else:
    print("Operacao invalida!")
    resultado = 0
print("Resultado: ", resultado)