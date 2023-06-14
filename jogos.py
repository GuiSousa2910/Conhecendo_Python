import random
import forca
import adivinhacao


asterisco = "*********************************"
print(asterisco)
print("Escolha qual jogo você quer jogar!")
print(asterisco)

print("(1) Adivinhação  (2) Forca")

jogo = int(input("Qual o jogo você gostara de jogar? \n"))

if(jogo == 1):
    #print("Bem vindo ao jogo de Adivinhação!")
    adivinhacao.jogar()
elif(jogo == 2):
    #print("Bem vindo ao jogo de Forca!")
    forca.jogar()
