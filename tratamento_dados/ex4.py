import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' ')[0])

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4] if len(x.split(' ')) >= 5 else 'Nenhum')

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

print(df['Desconto'].head())

# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: ''.join(char for char in x if char.isdigit())).replace('', 'nan')
print(df['Desconto'].head())
