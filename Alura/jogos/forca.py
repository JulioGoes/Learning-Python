import random


def jogar():

    mensagem()
    palavra_secreta = carrega_palavra_secreta()
    palavra_correta = inicializa_palavra_correta(palavra_secreta)

    palavra_final = [letra for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_final):
            marca_chute_correto(chute, palavra_final, palavra_correta)
            print('Você acertou! \n', palavra_correta)
        else:
            erros += 1
            print('Você errou! \n', palavra_correta)
            print(erros)

        enforcou = erros == len(palavra_final)
        acertou = "_" not in palavra_correta

        if enforcou is True:
            print('É uma pena, você perdeu!')

        if acertou is True:
            print('Parabéns, você venceu!')


def carrega_palavra_secreta():
    doc = open('src/doc.txt', 'r')
    palavra = [linha.strip().upper() for linha in doc]
    doc.close()

    num = random.randrange(0, len(palavra))
    palavra_secreta = palavra[num]
    return palavra_secreta


def mensagem():
    print('*********************************')
    print('***Bem-Vindo ao Jogo da Forca!***')
    print('*********************************')


def inicializa_palavra_correta(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_final, palavra_correta):
    index = 0
    for letra in palavra_final:
        if(chute == letra):
            palavra_correta[index] = chute
        index += 1


if __name__ == '__main__':
    jogar()
