# importando biblioteca para manuseio dos dados
import pandas as pd 

# criando tabela
tabela = pd.read_csv("Project2/clientes.csv", encoding="latin1", sep=";")

# removendo dados inúteis da tabela


tabela = tabela.drop("Unnamed: 8", axis=1)

print(tabela)

# Tratamento e visão geral dos dados

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

tabela = tabela.dropna()
print(tabela.info())



# Analisando os dados

print(tabela.describe())


import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", text_auto=True, histfunc="avg", nbins=10)
    grafico.show()