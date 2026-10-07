import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

df["total_vendas"] = df.groupby("vendedor")["vendas"].transform("sum")

df.loc[df["total_vendas"]>=3000, "desempenho"]="Bom"
df.loc[df["total_vendas"]<3000, "desempenho"]="Regular"

df["participacao"] = ((df["vendas"] / df["total_vendas"]) * 100).round(2)

df.loc[df["participacao"]<40, "status"] = "Baixa"
df.loc[df["participacao"]>=40, "status"] = "Media"
df.loc[df["participacao"]>=60, "status"] = "Alta"



print(df)