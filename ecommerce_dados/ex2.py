import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')
scaler = MinMaxScaler()

df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

df['Marca_Cod'] = LabelEncoder().fit_transform(df['Marca'])
df['Material_Cod'] = LabelEncoder().fit_transform(df['Material'])
df['Temporada_Cod'] = LabelEncoder().fit_transform(df['Temporada'])

# LabelEncoder → categorias → inteiros (cria ordem implícita)
# OneHotEncoder → categorias → colunas binárias (sem ordem)
# get_dummies → OneHotEncoder direto no pandas

