import pandas as pd

df = pd.read_csv('DIO_DataScience/arquivos_dio/Gapminder.csv', sep=';')
df = df.rename(columns={'country': 'Pais', 'continent': 'Continente',
                        'year': 'Ano', 'lifeExp': 'Expectativa de Vida',
                        'pop': 'População', 'gdpPercap': 'PIB'})

# print(df.head()) Retorna as 5 primeiras linhas ou o valor entre ()
# print(df.describe()) Retorna uma série de informações descritivas sobre os
# dados
#  print(df.shape) Retorna a quantidade de linhas e colunas
#  print(df.dtypes) Retorna o tipo de cada coluna
#  print(df.columns) Retorna o nome das colunas

# oceania = df.loc[df['Continente'] == 'Oceania']
# print(oceania.head())
# print(df.groupby('Continente')['Pais'].nunique()) Retorna a quantidade de
# pais por continente

# Retorna a media da Expectativa de Vida por ano
print(df.groupby('Ano')['Expectativa de Vida'].mean())
