def checa_cpf(cpf):
    # A função find() nos retorna um indice do valor passado como parametro
    # nesse caso, ela nós dira em qual indice se encontra o hífen -, que
    # no caso é 9
    separador = cpf.find('-')

    # Sabendo qual o indice do hífen, podemos colocar em outra variável
    # somente os primeiros digitos, sendo eles os quais iremos trabalhar
    primeiros_digitos = cpf[0:separador]

    # também é importando descobirmos os ultimos digitos para nossa
    # validação
    ultimos_digitos = cpf[10:]

    # a variável i serve apenas como um contador, ela inicia no 1
    # e é incrementada até o 9, iremos percorrer cada valor e multiplicá-lo
    # pelo valor da variável i, ou seja, o primeiro valor por 1, o segundo
    # por 2 e por aí vai, até o 9.
    i = 1

    # a variável soma irá armazenar as somas do nosso loop
    soma_digito1 = 0

    # no for a seguir, iremos percorrer cada número contigo na variável
    # primeiros_digitos, iremos converter esse número para um inteiro
    # em seguida multiplicá-lo pelo valor de i, esse valor é adicionado
    # a variável soma da seguinte forma:
    #  soma += (int(num) * i)
    #  soma 'recebe' = soma + (o valor de num transformado em inteiro) * i
    # o valor de soma é incrementada a cada repetição
    # o primeiro valor * 1 é alocado em soma, em seguida, o produto
    # do segundo valor * 2, depois o produto do terceiro * 3.
    for num in primeiros_digitos:
        soma_digito1 += (int(num) * i)
        i += 1

    # Agora temos que pegar o resto da divisão da soma por 11
    soma_digito1 = (soma_digito1 % 11)

    # A seguir, faremos exatamente a mesma coisa, a única mudança
    # é que o valor de i começa em 9 e é decrementado em 1 a cada
    # repetição
    i = 9
    soma_digito2 = 0
    for num in primeiros_digitos:
        soma_digito2 += (int(num) * i)
        i -= 1

    # Agora temos que pegar o resto da divisão da soma por 11
    soma_digito2 = (soma_digito2 % 11)

    # vamos criar variáveis que vão guardar nossas condições de True
    # lembrando que temos que converter os valores em ultimos_digitos
    # para inteiros, só assim poderemos comparar se elas são iguais
    # ao resto da soma

    # se o resto da soma for igual ao primeiro valor dos ultimos digitos (b1)
    # é true
    condicao1 = soma_digito1 == int(ultimos_digitos[0])

    # se o resto da soma for igual ao segundo valor dos ultimos digitos (b2)
    # é true
    condicao2 = soma_digito2 == int(ultimos_digitos[1])

    # se o resto da soma for igual a 10
    # e o primeiro valor dos ultimos digitos é igual a 0 (b1) é true
    condicao3 = soma_digito1 == 10 and ultimos_digitos[0] == 0

    # se o resto da soma for igual a 10
    # e o segundo valor dos ultimos digitos é igual a 0 (b1) é true
    condicao4 = soma_digito2 == 10 and int(ultimos_digitos[1]) == 0

    if (condicao1 and condicao2):
        return True
    elif (condicao1 and condicao4):
        return True
    elif (condicao2 and condicao3):
        return True
    else:
        return False


# vamos chamar nossa função com os cpfs do enunciado
print(checa_cpf('048856829-63'))
print(checa_cpf('733184680-96'))
print(checa_cpf('092844842-86'))
print(checa_cpf('098447895-55'))
