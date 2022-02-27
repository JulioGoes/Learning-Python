class Conta:

    # Método construtor, é chamado quando a classe é instânciada
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Método que retorna informações (alguns atributos)
    def extrato(self):
        print('Saldo {:.2f} | Titular {}'.format(self.__saldo, self.__titular))

    # Método que trabalha com um dos atributos
    def deposita(self, valor):
        self.__saldo += valor

    # Método que verifica se o valor a ser sacado está abaixo do limite
    # disponivel para saque
    def __pode_sacar(self, valor_a_ser_sacado):
        valor_de_saque_disponível = self.__saldo + self.__limite
        return valor_a_ser_sacado <= valor_de_saque_disponível

    # Método que realiza o saque caso o valor esteja abaixo do limite
    # e para isso, antes ele chama outro método para validar o valor
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite disponível'.format(valor))

    # Método que trabalha com outros objetos
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # Método get, retorna o valor de um atributo
    def get_saldo(self):
        return self.__saldo

    # Método get, retorna o valor de um atributo
    def get_titular(self):
        return self.__titular

    # Transformando a função em um atributo/propriedade
    @property
    def limite(self):
        return self.__limite

    # Alterando o valor do atributo com o setter
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'CAIXA': '104', 'BRADESCO': '237'}
