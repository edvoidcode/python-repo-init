#Escreva um jogo onde o computador escolhe um número, e você tenta adivinhar.
from random import randint

print ("### INICIANDO O JOGO ###")

random = randint(0, 15)
chute = 0
chances = 8

while chute != random:
    chute = input("Digite um numero de 1 a 15: ")
    if chute.isnumeric():
        chute = int(chute)
        chances = chances -1
        if chute == random:
            print("")
            print("Parabéns, você acertou! O numero era {} e voce ainda tinha {} chances.".format(random, chances))
            print("")
            break;
        else:
            print("")
            if chute > random:
                print("Você errou! Dica: é um número menor.")
            else:
                print("Você errou! Dica: é um número maior.")
            print("Você ainda tem {} chances.".format(chances))
            print("")
        if chances == 0:
            print("")
            print("Suas chances acabaram, você perdeu!!")
            print("")
            break;
print('#### Fim do Jogo ####')