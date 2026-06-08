import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dados = {
    "Ano" : [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Vendas" : [100, 120, 90, 150, 130, 170, 160]
}

df = pd.DataFrame(dados)

X = df[["Ano"]]
y = df["Vendas"]

modelo = LinearRegression()
modelo.fit(X, y)

anos_futuros = pd.DataFrame({"Ano": [2025, 2026, 2027, 2028]})

previsoes = modelo.predict(anos_futuros)

anos_futuros["Previsao"] = previsoes

print(anos_futuros)

plt.figure(figsize=(10, 5))

plt.plot(df["Ano"], df["Vendas"], marker='o', label="histórico")

plt.plot(anos_futuros["Ano"], anos_futuros["Previsao"], marker='o', linestyle='--', label="previsão")

plt.title("previsão de Vendas")
plt.xlabel("Ano")
plt.ylabel("Vendas")

plt.legend()
plt.grid(True)

plt.show()