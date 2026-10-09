import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

maior_venda = df.groupby("vendedor", as_index=False)["vendas"].sum().sort_values("vendas", ascending=False)

print(maior_venda)