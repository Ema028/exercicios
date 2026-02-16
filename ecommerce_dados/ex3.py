import pandas as pd

df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

map_vendidos = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(map_vendidos)
df['Marca_Freq'] = df['Marca'].map(df['Marca'].value_counts()/len(df))
df['Material_Freq'] = df['Material'].map(df['Material'].value_counts()/len(df))

# map(): converte texto → número com base em dicionário
# value_counts()/len(df): frequência relativa (0 a 1)
