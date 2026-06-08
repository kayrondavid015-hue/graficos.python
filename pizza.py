import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Quantidade de entrevistados
candidatos = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela"
]

#Quantidade de votos simulados
votos = np.random.randint(150, 350, size=4)

#Criando o DataFrame
df = pd.DataFrame({
    "Candidato" : candidatos,
    "Votos" : votos
})

#Calculando a porcentagem
df["Porcentagem"] = (df["Votos"] / df["Votos"].sum()) * 100

print(df)

#Criando o garfico de pizza
plt.figure(figsize=(8,8))

plt.pie(df["Votos"], labels=df["Candidato"], autopct="%1.1f%%")
plt.title("Pesquisa eleitoral simulada")
plt.show()