import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

media_vendedor = df.groupby("vendedor")["vendas"].mean()

print(media_vendedor.to_string(float_format="%.0f"))