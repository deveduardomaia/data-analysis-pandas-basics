import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

maior_valor = df.groupby("vendedor")["vendas"].sum().idxmax()

print(maior_valor)