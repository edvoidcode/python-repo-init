# Usando while
#Tarefa 3:
#Crie uma tabuada (1 a 10) para um número digitado pelo usuário.

operador = int(input("Digite um numero para tabuada de multiplicação: "))
x = 1
while x < 11:
    resultado = x * operador
    print(f"{operador} * {x} = {resultado}" )
    x += 1
