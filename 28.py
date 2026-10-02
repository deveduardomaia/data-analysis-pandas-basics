import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

grupo = df.groupby("vendedor")["vendas"].sum()

maior_venda = grupo.sort_values(ascending=False)

print(maior_venda.head(2).to_string())