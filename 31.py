import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

def classificar_vendas (vendas):
    if vendas >= 2000:
        return "Alta"
    else:
        return "Normal"

df["categoria"] = df["vendas"].apply(classificar_vendas)

print(df)