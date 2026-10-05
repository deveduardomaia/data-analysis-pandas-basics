import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

def classificar_vendas(vendas):
    if vendas >= 2500:
        return "Alta"
    elif vendas >=1500:
        return "Media"
    else:
        return "Baixa"

df["categoria"] = df["vendas"].apply(classificar_vendas)

print(df)