from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib


import pandas as pd
tabela = pd.read_csv(
    r'C:\Users\Igor\Desktop\Python\Dungeons-e-Codes\Hashtag Treinamentos\Base de dados hastag\advertising.csv')
print(tabela)
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)
plt.show()

y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.3, random_state=1)


modelo_regressaolinear = LinearRegression()
modelo_arvorededecisao = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvorededecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvorededecisao = modelo_arvorededecisao.predict(x_teste)

print(metrics.r2_score(y_teste, previsao_arvorededecisao))
print(metrics.r2_score(y_teste, previsao_regressaolinear))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsao de Regresso Linear'] = previsao_regressaolinear
tabela_auxiliar['Previsao arvore de decisao'] = previsao_arvorededecisao

plt.figure(figsize=(15, 6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

nova_tabela = pd.read_csv(
    r'C:\Users\Igor\Desktop\Estudos\Python\Hashtag Treinamentos\Base de dados hastag\Novos.csv')
previsao = modelo_arvorededecisao.predict(nova_tabela)
print(previsao)
