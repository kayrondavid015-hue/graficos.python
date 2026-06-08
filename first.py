import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

df = pd.DataFrame({
    "idade": np.random.randint(18, 60, n),
    "Salario": np.random.randint(1500, 8000, n),
})

df["compras"] = ((df["Salario"] / 1000) * 0.8 + (df["idade"] / 10) * 0.5 + np.random.randn(n) * 2).astype(int)

df["compras"] = df["compras"].clip(lower=0)

#print(df.head())

from sklearn.cluster import KMeans

X = df[["idade", "Salario", "compras"]]

kmeans = KMeans(n_clusters=3, random_state=42)

df["Cluster"] = kmeans.fit_predict(X)

#print(df.head())

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df["idade"], df["Salario"], df["compras"], c=df["Cluster"], cmap="viridis")

ax.set_xlabel("idade")
ax.set_ylabel("Salario")
ax.set_zlabel("Compras")
ax.set_title("Clusters de Clientes")

plt.show()

resumo = df.groupby("Cluster").mean()
print(resumo)

mapa = {
    1: "VIP",
    2: "Padrão",
    0: "Baixo"
}

df["Tipo_Cliente"] = df["Cluster"].map(mapa)
print(df.head())