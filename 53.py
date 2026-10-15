import pandas as pd

dados = {
    "vendedor": ["Ana", "João", "Ana", "Pedro", "João"],
    "vendas": [1000, 2000, 1500, 3000, 1000]
}

df = pd.DataFrame(dados)

agrupar = df.groupby("vendedor", as_index=False)["vendas"].sum()
maior_valor = agrupar["vendas"].max()

resultado = agrupar[agrupar["vendas"]==maior_valor]

print(resultado)