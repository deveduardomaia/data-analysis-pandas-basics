import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

resultado = df[(df["vendas"] > 1000) & (df["vendas"] < 3000)]

print(resultado)