import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

df.loc[(df["vendas"]>=2000) & (df["vendedor"]=="João"), "classificacao"] = "Destaque"
df.loc[(df["vendas"]>=2000) & (df["vendedor"]!="João"), "classificacao"] = "Alta"
df.loc[df["vendas"]<2000, "classificacao"]= "Normal"

print(df)