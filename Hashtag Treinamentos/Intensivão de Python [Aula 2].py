# Analise de dados

import pandas
import plotly.express as px
import pandas as pd

tabela = pandas.read_csv(
    r"C:\Users\Igor\Desktop\Estudos\Programação em Python\Hashtag Treinamentos\Base de dados hastag\Telecom_users.csv")
print(tabela)

# O que não tSe ajuda te atrapalha
# axis = 0 --> linha
# axis = 1 __> coluna
tabela = tabela.drop('Unnamed: 0', axis=1)
print(tabela)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()
