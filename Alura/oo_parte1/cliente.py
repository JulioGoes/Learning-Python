class Cliente:

    #  Método construtor
    def __init__(self, nome):
        self.__nome = nome

    # @property transforma a função nome() em propriedade
    # é possível chamá-la sem a necessidade de '()'
    @property
    def nome(self):
        return self.__nome.title()

    # @nome.setter altera o valor do atributo nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
