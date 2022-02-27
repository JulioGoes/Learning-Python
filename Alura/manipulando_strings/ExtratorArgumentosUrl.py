class ExtratorArgumentosUrl:

    # Criamos o objeto da Url, mas antes, verificamos se ela existe
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url Inválida')

    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        moO, moD = self.extraiArgumentos()
        teste = f'Moeda Origem: {moO} | Moeda Destino: {moD}'
        representaçãoString = teste + f' | Valor: {self.extraiValor()}'
        return representaçãoString

    # def __eq__(self, outraInstancia: object) -> bool:
    #     return self.url == outraInstancia.url

    # O método estático a seguir, verifica se a url é vazia ou nula
    # Se não for, o método retorna True
    @staticmethod
    def urlEhValida(url):

        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    # O método a seguir extrai os valores que queremos da Strings
    def extraiArgumentos(self):

        # As variaveis a seguir são os parametros e nós estamos buscando
        # os valores
        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        # A seguir, fazemos uma busca do indice inicial e final do valor
        # usando a variavel Busca como referência
        indiceInicialMoedaOrigem = self.buscaMoeda(buscaMoedaOrigem)
        indiceFMoedaOrigem = self.url.find("&")

        # A mesma coisa é feita com o próximo valor a ser buscado
        indiceInicialMoedaDestino = self.buscaMoeda(buscaMoedaDestino)
        indiceFMoedaDestino = self.url.find("&valor=")

        # A seguir, pegamos os valores da String, usando o indice inicial
        # e final como base, e alocamos esses valores em variaveis
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFMoedaDestino]

        # Caso seja verificado que um dos valores esteja alterado
        # alteramos esse valor pelo valor que deferia ser, e fazemos o mesmo
        # processo anterior
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.buscaMoeda(buscaMoedaOrigem)
            indiceFMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFMoedaOrigem]

        # retornamos os valores capturados da string
        return moedaOrigem, moedaDestino

    # O método a seguir faz a busca na string atrás dos valores
    def buscaMoeda(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    # Caso tenha valores incorretos, o método a seguir faz a troca
    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        IndiceInicialValor = self.buscaMoeda(buscaValor)
        valor = self.url[IndiceInicialValor:]
        return valor
