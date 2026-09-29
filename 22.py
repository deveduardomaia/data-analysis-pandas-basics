import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

resultado = df[(df["vendas"] >= 1500) & (df["vendedor"] == "Ana")]

print(resultado)