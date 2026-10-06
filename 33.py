import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

def calcular_bonus(vendas):
    if vendas >= 2000:
        return vendas * 0.10
    else:
        return vendas *0.05

df["bonus"] = df["vendas"].apply(calcular_bonus).astype(int)

print(df)