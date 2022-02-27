# Criando a classe Pai
class Programa:

    # Método construtor da classe Pai
    # será herdado nos objetos das classes Filhas
    def __init__(self, nome, ano):
        self.nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Os métodos da classe Pai podem ser usados nas classes Filhas
    # como se fossem delas
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


# É necessário colocar entre () a classe Pai na herança
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        # A função super cria a instancia do método construtor da classe Pai
        # é necessário mandar os paramêtros.
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self.likes} (Y)'


class Serie(Programa):

    def __init__(self, nome, ano, temp):
        super().__init__(nome, ano)
        self.temp = temp

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temp} - {self.likes} (Y)'


class Playlist():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Transforma o objeto em iterável através de Duck Typing
    def __iter__(self):
        return iter(self._programas)

    # Faz com que o objeto saiba informar seu próprio tamanho
    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
homem_de_ferro = Filme('homem de ferro', 2008, 126)
aranhaverso = Filme('homem-aranha no aranhaverso', 2018, 96)
atlanta = Serie('atlanta', 2018, 2)

series_e_filmes = [vingadores, homem_de_ferro, aranhaverso, atlanta]
playlist_fim_de_semana = Playlist('Fim de Semana', series_e_filmes)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')
