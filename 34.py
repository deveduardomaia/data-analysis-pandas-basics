import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

def percentual(vendas):
    if vendas >=2000:
        return "10%"
    else:
        return "5%"

df["bonus_percentual"] = df["vendas"].apply(percentual)

print(df)