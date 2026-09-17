import pandas as pd

dados = {
    "produto": ["Notebook","Mouse","Teclado","Monitor"],
    "preco": [3500, 80, 150, 1200],
    "quantidade": [2, 10, 5, 3],
}

df = pd.DataFrame(dados)

df["total"] = df["preco"] * df["quantidade"]

print(df)