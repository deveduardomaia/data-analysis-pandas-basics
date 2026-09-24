import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

vendedor_superior = df.groupby("vendedor")["vendas"].sum()

print(vendedor_superior[vendedor_superior>=3000].to_string())