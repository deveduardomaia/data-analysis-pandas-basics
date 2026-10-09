import pandas as pd

dados = {
    "produto": ["Celular", "Tablet", "Fone", "Cabo", "Notebook"],
    "preco": [2000, 1200, 300, 50, 3500],
    "quantidade": [3, 2, 5, 10, 2]
}

df = pd.DataFrame(dados)

df["valor_venda"] = df["preco"] * df["quantidade"]

maior_preco = df[df["preco"] > 1000].sort_values("valor_venda", ascending=False)[["produto", "valor_venda"]]

print(maior_preco)