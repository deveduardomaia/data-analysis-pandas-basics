import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

media_vendas = df.groupby("vendedor", as_index=False)["vendas"].mean().sort_values("vendas", ascending=False)

media_maior = media_vendas[media_vendas["vendas"]>1300]

print(media_maior)