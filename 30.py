import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

grupo = df.groupby("vendedor")["vendas"].mean().astype(int)

media = grupo[grupo>1400].to_string()

print(media)