import forca
import index

print("E scolha o jogo")

print("(1)Forca (2)Adivinhação")

jogo = int(input("->"))

if(jogo == 1):
    print("Forca")
    forca.jogo_forca()
elif(jogo == 2):
    print("Adivinhação")
    index.jogo_Adv()