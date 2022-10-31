import os
from random import random
from re import S

print("Bem vindo ao jogo da forca!")
Desafiante = str(input('Informe o nome do desafiante para começar: '))
Jogador = str(input('Informe o nome do competidor para começar: ')) 

def leitura_palavra_secreta():
    arquivo = open('lista.txt', "r")
    palavras = []

    for linha in arquivo:
        linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

os.system("cls")

print ("SOMENTE LETRAS MAIUSCULAS!")
palavraChave = str(input("Digite a palavra chave: "))

os.system("cls")

dica1 = str(input("Escreva a primeira dica: "))
dica2 = str(input("Escreva a segunda dica: "))
dica3 = str(input("Escreva a terceira dica: "))


digitadas = []
chances = 5

print("Digite apenas numero")
print("O que deseja fazer?")
print("1. Dica")
print("2. Jogar")
opcao = input(": ")

if(not opcao.isalpha()):
    opcao = int(opcao)
    if(opcao < 0 or opcao > 2):
        print("!Opcao invalida!")

    if (opcao == 1):
        print (dica1)
        print (dica2)
        print (dica3)

while True:

    if chances <= 0:
        print("O Desafiante ganhou!")
        break
    letra = input(f' ( JOGO DA FORCA ) - Você tem apenas {chances} chances.  Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas um carácter')
        continue

    digitadas.append(letra)

    if letra in palavraChave:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'Essa letra {letra} NÃO EXISTE')
        digitadas.pop()
        chances = chances - 1

    palavraChave_temporario = ''
    for letra_secreta in palavraChave:
        if letra_secreta in digitadas:
            palavraChave_temporario += letra_secreta
        else:
            palavraChave_temporario += '*'


    if palavraChave_temporario == palavraChave:
        print("O competidor Ganhou!")
        break
    else:
        print(f'A palavra secreta está assim {palavraChave_temporario}')

while True: 
    print ("1 - Obrigado por jogar")
    print ("2 - Sair")
    opcao = int(input("> ")) 
    if (opcao == 1): break
    elif (opcao == 2): break  
    else: print ("Opcao invalida!")
os.system("cls")