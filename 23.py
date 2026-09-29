import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

resultado = df[(df["vendedor"] == "Ana") | (df["vendas"] > 2000)]

print(resultado)

