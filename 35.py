import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

df.loc[df["vendas"]>=2500, "nivel"]="Alta"
df.loc[df["vendas"]>=1500, "nivel"]="Media"
df.loc[df["vendas"]<1500, "nivel"]="Baixa"

print(df)