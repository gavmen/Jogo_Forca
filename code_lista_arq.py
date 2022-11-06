import random

arquivo = open("Forca\Lista-de-Palavras.txt", "r")
lista_palvras = arquivo.read().splitlines()

pal = random.choice(lista_palvras)
pal = pal.lower()
jogo = True
lista = list(pal)
lst_player = list(pal)
index = 0
vida = 8
acerto = False

print('Caso deseje chutar a palavra, digite chute\nCuidado, caso erre, perderá o jogo!')

for i in range(len(lst_player)):
    lst_player[index] = '_'
    index += 1

print(str(lst_player).replace(' [', '').replace('[', '').replace(']', '').replace(',', ' '))
index = 0


while jogo == True:
    letra = input('Escolha uma letra: ')
    for i in range(len(lista) + 1):
        if letra == lista[index]:
            lst_player[index] = lista[index]
            acerto = True
            if index == len(lista)-1:
                index = 0
            else:
                index += 1
        else:
            if index == len(lista)-1:
                index = 0
            else:
                index += 1
    if letra == 'chute':
        chute = list(input('Digite uma palavra para chutar: '))
        if chute == lista:
            print('Vc Ganhou!')
            print('A palavra era:', pal)
            jogo = False
            break
        else:
            print('Vc Perdeu!')
            print('A palavra era:', pal)
            jogo = False    
            break
    if acerto == True:
        vida += 1
    if lst_player == lista:
        print('Vc ganhou!')
        jogo = False
    else:
        vida -= 1
        print('Vc ainda tem' ,vida, 'vidas!')
        if vida <= 0:
            print('Vc Perdeu!')
            print('A palavra era:', pal)
            jogo = False
    acerto = False
    print(str(lst_player).replace(' [', '').replace('[', '').replace(']', '').replace(',', ' '))
