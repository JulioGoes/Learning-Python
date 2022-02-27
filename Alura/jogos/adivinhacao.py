from random import randrange


def jogar():
    secret_number = randrange(1, 30)
    num_tentativas = 0
    condicao = 1
    chute = 0

    print('*********************************')
    print('Bem-Vindo ao Jogo de Adivinhação!')
    print('*********************************')

    while condicao == 1:
        print('Escolha a dificuldade:')
        nivel = int(input('(1) Fácil, (2) Normal ou (3) Difícil: '))

        if nivel == 1:
            num_tentativas = 20
            condicao = 0
        elif nivel == 2:
            num_tentativas = 10
            condicao = 0
        elif nivel == 3:
            num_tentativas = 5
            condicao = 0
        else:
            print('Você digitou um valor incorreto!')
            print('*********************************')

    while num_tentativas > 0:

        print('*********************************')
        print('Tentativas restantes: {0}'.format(num_tentativas))

        chute = int(input('Digite um número entre 1 e 30: '))
        print('*********************************')

        if chute < 1 or chute > 30:
            print('Você digitou um valor inválido!')
            print('*********************************')
            continue

        acertou = secret_number == chute
        errou_maior = chute > secret_number

        if (acertou):
            print('Parabéns! O número correto é: {}'.format(str(chute)))
            print('Fim do Jogo')
            break
        else:
            if (errou_maior):
                print('Você errou! O número secreto é menor.')
            else:
                print('Você errou! O número secreto é maior.')

        num_tentativas = num_tentativas - 1


if __name__ == '__main__':
    jogar()
