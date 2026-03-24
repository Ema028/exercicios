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
# MinMaxScaler -> espreme todos os seus dados para caberem dentro de uma caixa exata, geralmente entre 0 e 1.
# StandardScaler -> ajusta a sua coluna para que a média de todos os valores passe a ser 0 e o desvio padrão seja 1.
