import pandas as pd

dados = {
    "produto": ["Celular", "Tablet", "Fone", "Cabo", "Notebook"],
    "preco": [2000, 1200, 300, 50, 3500],
    "quantidade": [3, 2, 5, 10, 2]
}

df = pd.DataFrame(dados)

df["valor_venda"] = df["preco"] * df["quantidade"]

print(df["valor_venda"].max())