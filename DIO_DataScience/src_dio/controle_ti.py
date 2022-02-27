import pandas as pd

df = pd.read_csv('DIO_DataScience/arquivos_dio/estudos.csv', sep=';')

print(df.head())

df['Dia'] = pd.to_datetime(df['Dia'])
print(df.dtypes)

print(df.shape)
