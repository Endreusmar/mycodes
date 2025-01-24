import random
#criar uma lista de palavras que serão sorteadas
palavras = ['Python','Geysiane','Endreus','galão','dinheiro']

palavras_sorteada = random.choice(palavras)
palavras_sorteada

#criar uma string que substitui as letras por '-'.

palavra_escondida = '-' *len(palavras_sorteada)

#criamos uma lista vazia para armazenas as letras que já foram tentadas

letras_advinhadas = []

max_tentativas = 6

while True:
    #mostrar na tela a palavra escondida
    print(palavra_escondida)


    #pedimos ao jogador pra digitar uma letra
    letra = input('Digite uma letra, camarada e tente não ser enforcado.')

    #verificamos se a letra informada já foi digitada
    if letra in letras_advinhadas:
        print('você já digitou essa letra, digite outra mané.')
        continue
    #add a letra da lista de letras digitadas
    letras_advinhadas.append(letra)

    #verificar se a letra digitada está na palavra sorteada

    if letra in palavras_sorteada:
        lista = []
    for indice in range(len(palavras_sorteada)):
        if letra == palavras_sorteada[indice]:
                lista.append(letra)
        else:
                lista.append(palavra_escondida[indice])
                palavra_escondida = '-'.join(lista)
                #letra não esta na palavra sorteada
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada, você agora possui{max_tentativas}tentativas')

                #verificamos se o jogador ganhou ou perdeu
    if palavra_escondida == palavras_sorteada:
        print('Parabéns, você acertou a palavra e não foi enforcado')
        break
    elif max_tentativas == 0:
        print ('Cara, te dei a chance e você não acertou, vai morrer.')
        break




                

                


                
            
            



            
