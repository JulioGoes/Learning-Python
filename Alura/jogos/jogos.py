import adivinhacao
import forca

print('*****************************************************')
print('***Seja bem vindo! Escolha o jogo que deseja jogar***')
valor = int(input('(1) Adivinhação | (2) Forca: '))

if valor == 1:
    adivinhacao.jogar()
elif valor == 2:
    forca.jogar()
else:
    print('Valor inválido')
