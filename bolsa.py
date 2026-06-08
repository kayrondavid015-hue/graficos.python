import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(42)

dias = 30

datas = pd.date_range(start="2026-01-01", periods=dias)

empresas = {
    "TechX": [100],
    "FoodCorp" : [80],
    "AutoDrive": [120]
}

noticias = {
    "TechX": [
        ("Nova IA revolucionária", 15),
        ("Ataque hacker", -20),
        ("Lucro recorde", 10)
    ],
    "FoodCorp": [
        ("Produto viralizou", 8),
        ("Problema sanitário", -15),
        ("Expansão internacional", 10)
    ],
    "AutoDrive": [
        ("Novo carro elétrico", 12),
        ("Recall de veículos", -18),
        ("Parceria internacional", 9)
    ]
}

for i in range(dias - 1):
    for nome in empresas:

        ultimo_preco = empresas[nome][-1]

        variacao = np.random.randint(-5, 6)

        if random.random() < 0.3:

            noticia, impacto = random.choice(noticias[nome])

            print(f"Dia {i+1} | {nome}: {noticia} ({impacto})")

            variacao += impacto

        novo_preco = ultimo_preco + variacao

        novo_preco = max(novo_preco, 1)

        empresas[nome].append(novo_preco)

df = pd.DataFrame({"Data": datas, "TechX": empresas["TechX"], "FoodCorp": empresas["FoodCorp"], "AutoDrive": empresas["AutoDrive"]})

plt.figure(figsize=(12, 6))

plt.plot(df['Data'], df["TechX"], label="TechX")
plt.plot(df["Data"], df["FoodCorp"], label="FoodCorp")
plt.plot(df["Data"], df["AutoDrive"], label="AutoDrive")

plt.title("Bolsa simulada com  notícias")
plt.xlabel("Data")
plt.ylabel("Preço da Ação")

plt.legend()
plt.grid(True)

plt.show()

ranking = {
    nome: empresas[nome][-1]
    for nome in empresas
}

ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

print("\nRanking final: \n")
for posicao, (nome, preco) in enumerate(ranking_ordenado, start=1):
    print(f"{posicao}. {nome} -> ${preco}")