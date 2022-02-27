import pandas as pd
from matplotlib import pyplot as plt

# Lendo arquivos do excel e salvando-os em uma variável
df1 = pd.read_excel('DIO_DataScience/arquivos_dio/Aracaju.xlsx')
df2 = pd.read_excel('DIO_DataScience/arquivos_dio/Fortaleza.xlsx')
df3 = pd.read_excel('DIO_DataScience/arquivos_dio//Natal.xlsx')
df4 = pd.read_excel('DIO_DataScience/arquivos_dio/Recife.xlsx')
df5 = pd.read_excel('DIO_DataScience/arquivos_dio/Salvador.xlsx')

# print(df1.head())
# print(df2.head())

# Concatenando planilhas
df = pd.concat([df1, df2, df3, df4, df5])

# print(df.sample(5)) Retorna uma 'amostra', ou melhor,
# algumas linhas aleatórias de nossa planilha de dados


# Altera o tipo de dado da coluna indicada
df['LojaID'] = df['LojaID'].astype('object')

# Retorna o tipo de dado de cada coluna
# print(df.dtypes)
# print('****************')

'''
    Trabalhando com valores nulos >>>
'''

# Consultado se há valores nulos em nossa planilha de dados
# print(df.isnull().sum())
# print('****************')

# Substituindo valores nulos pela média geral da coluna
# O resultado seria um número com muitas casas decimais a função round()
# arredonda o valor
# df['Vendas'].fillna(round(df['Vendas'].mean()), inplace=True)

# Substituindo os valores nulos por zero
df['Vendas'].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
# df.dropna(inplace=True)

# Apagando as linhas com valores nulos tendo como base somente 1 coluna
# df.dropna(subset=['Vendas'], inplace=True)

# Removendo linhas com valores nulos em todas as colunas
# df.dropna(how='all', inplace=True)


'''
    Criando novas Colunas e trabalhando com estátistica >>
'''

# Criando a coluna de receita, sendo o produto de vendas e quantidade
df['Receita'] = df['Vendas'].mul(df['Qtde'])

# print(df.head())

# Retorna o maior valor de uma coluna
# print(df['Receita'].max())

# Retorna o menor valor de uma coluna
# print(df['Receita'].min())

# Retorna as linhas com os maiores valores em uma coluna
# print(df.nlargest(3, 'Receita'))

# Retorna as linhas com os menores valores em uma coluna
# print(df.nsmallest(3, 'Receita'))
# print('****************')

# Retorna a soma dos valores de uma coluna agrupados
# print(df.groupby('Cidade')['Receita'].sum())
# print('****************')

# Ordena os maiores valore de uma coluna em ordem, do menor para o maior
# print(df.sort_values('Receita', ascending=False).head(10))

# Retorna a soma da receita por ano da coluna data
# print(df.groupby(df['Data'].dt.year)['Receita'].sum())

# Cria uma coluna para dia/mês/ano
df['Ano Venda'] = df['Data'].dt.year
df['Mês Venda'] = df['Data'].dt.month
df['Dia Venda'] = df['Data'].dt.day

# Calculando a diferença de datas
df['Diferença de Datas'] = df['Data'] - df['Data'].min()

# Filtra os registros com condicionais
vendas = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]
# print(vendas.sample(20))

# Retorna a data mais antiga/mais recente
# print(df['Data'].max())

# Retorna um gráfico de barras horizontais
# df['LojaID'].value_counts(ascending=True).plot.barh()
# Retorna um gráfico de barras
# df['LojaID'].value_counts(ascending=True).plot.bar()
# Retorna um gráfico de pizza
# df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie()
# Imprime o gráfico

# Adicionando um título, aletando a cor e mudando o nome dos eixos
# df['Cidade'].value_counts().plot.bar(title='Vendas por Cidade', color='red')
# plt.xlabel('Cidade')
# plt.ylabel('Total Vendas')
# plt.show()

# Alterando o estilo do gráfico
# plt.style.use('ggplot')
# df.groupby(df['Mês Venda'])['Qtde'].sum().plot()
# plt.xlabel('Mês')
# plt.ylabel('Total Produtos Vendidos')
# plt.legend()
# plt.show()

# Selecionando apenas as vendas de 2019
df_2019 = df[df['Ano Venda'] == 2019]

# Total de produtos vendidos por mês
df_2019.groupby(df_2019['Mês Venda'])['Qtde'].sum().plot(marker='v')
plt.title('Total Vendas x Mês')
plt.xlabel('Mês')
plt.ylabel('Total Produtos Vendidos')
plt.legend()
plt.savefig('DIO_DataScience/src_dio/qtde_x_mes.png')
plt.show()

# Fazendo um histograma
# plt.hist(df['Qtde'], color='yellow')
# plt.show()
