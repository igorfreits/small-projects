from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from data import lista_de_carros, c
from time import sleep
from sklearn import metrics


class estacionamento:
    def __init__(self):

        self.a1 = {'Vaga': 1, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a2 = {'Vaga': 2, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a3 = {'Vaga': 3, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

    def adicionar_carro(self, carro, placa):
        self.carro = carro
        self.placa = placa = c
        if self.carro in lista_de_carros:
            if self.a1['Status'] == 'Ocupado':
                if self.a2['Status'] == 'Ocupado':
                    if self.a3['Status'] == 'Livre':
                        self.a3['Carro'] = self.carro
                        self.a3['Placa'] = self.placa
                        self.a3['Status'] = 'Ocupado'
                        print(
                            '\033[32mSeu carro foi adicionado na vaga 3\033[m')
                    else:
                        print('\033[31mEstacionamento lotado!\033[m')

            if self.a1['Status'] == 'Ocupado':
                if self.a2['Status'] == 'Livre':
                    self.a2['Carro'] = self.carro
                    self.a2['Placa'] = self.placa
                    self.a2['Status'] = 'Ocupado'
                    print('\033[32mSeu carro foi adicionado na vaga 2\033[m')

            if self.a1['Status'] == 'Livre':
                self.a1['Carro'] = self.carro
                self.a1['Placa'] = self.placa
                self.a1['Status'] = 'Ocupado'
                print('\033[32mSeu carro foi adicionado na vaga 1\033[m')

        else:
            print('\033[31mNome de carro invalido\033[m')
            sleep(1)

    def vagas(self):
        print(self.a1)
        print()
        print(self.a2)
        print()
        print(self.a3)

    def remover_carro(self, vaga=0):
        self.vagas()
        sleep(1)
        vaga = int(
            input('Digite o nome da vaga que você quer remover o carro: '))

        if vaga == 1:
            self.a1['Status'] = 'Livre'
            self.a1['Carro'] = None
            self.a1['Placa'] = None
            print('\033[32mVaga 1 liberada\033[m')
        if vaga == 2:
            self.a2['Status'] = 'Livre'
            self.a2['Carro'] = None
            self.a2['Placa'] = None
            print('\033[32mVaga 2 liberada\033[m')
        if vaga == 3:
            self.a3['Status'] = 'Livre'
            self.a3['Carro'] = None
            self.a3['Placa'] = None
            print('\033[32mVaga 3 liberada\033[m')

    def liberar(self):
        self.a1['Status'] = 'Livre'
        self.a1['Carro'] = None
        self.a1['Placa'] = None

        self.a2['Status'] = 'Livre'
        self.a2['Carro'] = None
        self.a2['Placa'] = None

        self.a3['Status'] = 'Livre'
        self.a3['Carro'] = None
        self.a3['Placa'] = None

        print('Todas as vagas foram liberadas!')

    def relatorio(self):

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


teste = estacionamento()
