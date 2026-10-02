import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

grupo = df.groupby("vendedor")["vendas"].sum()

maior_vendedor = grupo[grupo>=3000].sort_values()

print(maior_vendedor.to_string())