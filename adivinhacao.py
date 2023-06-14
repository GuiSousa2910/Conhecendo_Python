import random
import string 

def jogar():
    asterisco = "*********************************"
    print(asterisco)
    print("Bem vindo ao jogo de adivinhação!")
    print(asterisco)

    numeroSecreto = random.randrange(1, 101)
    totalDeTentativas = 0
    maximoTentativas = 0
    pontos = 100

    print("Qual nível de dificuldade você gostaria de jogar? \n" 
        , "(1) Fácil (2) Médio (3) Difícil")

    while (totalDeTentativas == 0):
        nivel = int(input('Defina o nível: '))

        if(nivel == 1):
            maximoTentativas = 15
            totalDeTentativas = maximoTentativas
        elif(nivel == 2):
            maximoTentativas = 10
            totalDeTentativas = maximoTentativas
        elif(nivel == 3):
            maximoTentativas = 5
            totalDeTentativas = maximoTentativas
        else:
            print("Digite um número valido.")
        

    for rodada in range(1, totalDeTentativas + 1) :
        #print("ESSE AQUI: " , numeroSecreto)

        print("Tentativa ", rodada, "de:" , totalDeTentativas)
        chuteString = input("Digite seu número: ")

        chute = int(chuteString)
        print('Você tentou o número' , chute)

        if(chute < 1 ):
            print("Você deve digitar um número maior que 1")
            continue

        if(chute > 100):
            print("Você deve digitar um número menor que 100")
            continue

        acertou = numeroSecreto == chute
        foiMaior = chute > numeroSecreto
        foiMenor = chute < numeroSecreto

        if (acertou):
            print("Você acertou! E fez", pontos, "pontos" )
            break
            #jogarNovamente = string(input("Você gostaria de jogar novamente? \n"))
            #if(jogarNovamente == "sim" , "gostaria" , "SIM" , "Sim" , "s" , "S"):
                #jogoAdivinhacao()
            
        elif(rodada == totalDeTentativas):
            print("Você perdeu! O número correto era", numeroSecreto)
            break
            
        else: 
            if(foiMaior):
                print("Você errou! O seu número foi maior do que esperado")
            elif(foiMenor):
                print("Você errou! O seu número foi menor do que esperado")
            pontosPerdidos = abs(numeroSecreto - totalDeTentativas)
            pontos = abs(pontos - pontosPerdidos)

            
        rodada = rodada + 1

if(__name__ == "__main__"):
    jogar()
