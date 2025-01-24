#Jogo da forca
import random

palavras = ['Python', 'Geysiane', 'Endreus', 'galão', 'dinheiro']
palavra_sorteada = random.choice(palavras)  
palavra_escondida = '-' * len(palavra_sorteada)
letras_advinhadas = []
max_tentativas = 6

while True:
    print(palavra_escondida)
    letra = input('Digite uma letra: ')  

    if letra in letras_advinhadas:
        print('Você já digitou essa letra.')
        continue

    letras_advinhadas.append(letra)
    acertos = 0

    nova_palavra = ""
    for i, letra_palavra in enumerate(palavra_sorteada):
        if letra == letra_palavra:
            nova_palavra += letra
            acertos += 1
        else:
            nova_palavra += palavra_escondida[i]

    palavra_escondida = nova_palavra

    if acertos > 0:
        print(f"Acertou {acertos} letra(s)!")
    else:
        max_tentativas -= 1
        print(f"Letra não encontrada. Restam {max_tentativas} tentativas.")

    if palavra_escondida == palavra_sorteada:
        print("Parabéns, você venceu!")
        break
    elif max_tentativas == 0:
        print(f"Você perdeu! A palavra era {palavra_sorteada}.")
        break
