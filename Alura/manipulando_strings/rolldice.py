rolagem = '1d20+2'
index = rolagem.find('d')

if rolagem.find('+'):
    index_2 = rolagem.find('+')
elif rolagem.find('-'):
    index_2 = rolagem.find('-')
else:
    pass

if index_2 != -1:

    quant = rolagem[:index]
    dado = rolagem[index + 1:index_2]
    soma = rolagem[index_2 + 1:]
    mod = rolagem[index_2]
    print(rolagem)
    print(quant, 'd', dado, mod, soma)
else:

    quant = rolagem[:index]
    dado = rolagem[index + 1:]
    print(rolagem)
    print(quant, 'd', dado)

print('************')
