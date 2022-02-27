from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# Criamos uma variável com uma url, onde teremos que buscar nessa Strings
# os valores de moeda origem e moeda destino
site = 'https://bytebank.com/'
url = site + 'cambio?moedaorigem=real&moedadestino=dolar&valor=1500'

# Fazemos a instância da classe passando a url como parametro
argumentos = ExtratorArgumentosUrl(url)
argumentos2 = ExtratorArgumentosUrl(url)

# Chamamos um método da classe, e alocamos seu retorno em duas variáveis
moedaorigem, moedadestino = argumentos.extraiArgumentos()
valor = argumentos.extraiValor()

# Imprimimos essas variáveis na tela
# print(f'Moeda Origem: {moedaorigem} | Moeda Destino: {moedadestino}')
# print(f'Valor: {valor}')

# print(len(argumentos))
# print(argumentos)
print(id(argumentos))
print(id(argumentos2))
print(argumentos == argumentos2)
