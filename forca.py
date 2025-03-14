import random

def jogo_forca():
    
    ImprimeMenssagem()
    
    palavra_secreta = carregaPalavra()

    letra_acertadas = EscopoDeSenha(palavra_secreta)
    print(letra_acertadas)
   
    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pedir_a_entrada()

        if(chute in palavra_secreta):
            substituicao_letras(palavra_secreta,chute,letra_acertadas)
        else:
            erros = erros + 1 
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letra_acertadas
        
        print(letra_acertadas)
    

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def ImprimeMenssagem():
    print("********************************")
    print("***Bem vindo ao Jogo da forca***")
    print("********************************")

def carregaPalavra():
    arquivo = open("palavras.txt" , "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
    
def EscopoDeSenha(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pedir_a_entrada():
    chute =input("Qual a letra quer chutar ?")
    chute = chute.strip().upper()
    return chute

def substituicao_letras(palavra_secreta, chute, letra_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute  == letra):
            letra_acertadas[index] = letra
        index = index + 1
         

if(__name__ == "__main__"): #isso é para funcionar mesmo sem o jogos.py
    jogo_forca()
