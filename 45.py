import pandas as pd

dados = {
    "produto": ["Celular", "Tablet", "Fone", "Cabo", "Notebook"],
    "preco": [2000, 1200, 300, 50, 3500],
    "quantidade": [3, 2, 5, 10, 2]
}

df = pd.DataFrame(dados)

df["valor_venda"] = df["preco"] * df["quantidade"]

resultado = df.sort_values("valor_venda", ascending=True).head(3)[["produto", "valor_venda"]]

print(resultado)