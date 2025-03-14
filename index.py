import random

def jogo_Adv():
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuladade?")
    print("(1)Facíl(2)Médio(3)Difícil")

    nivel = int(input("->"))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1) :
        print(numero_secreto)
        print("tentativa {} de {}" .format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu numero: ")
        print("Voce digitou " , chute_str)
        chute = int(chute_str)  

        if(chute < 1 or chute > 100):
            print(" o número é entre 1 e 100")  
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou!! e você fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("o numero que você chutou é maior do que o sortedo")
            elif(menor):
                print("o numero que você chutou é menor do que o sortedo")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos        
        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"): #isso é para funcionar mesmo sem o jogos.py
    jogo_Adv()


