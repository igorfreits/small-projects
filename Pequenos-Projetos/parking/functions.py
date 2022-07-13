from data import lista_de_carros, gerador
from time import sleep
from datetime import datetime


class estacionamento:
    def __init__(self):

        self.vaga = {
            'parking1': {'Vaga': 1, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking2': {'Vaga': 2, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking3': {'Vaga': 3, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking4': {'Vaga': 4, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking5': {'Vaga': 5, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking6': {'Vaga': 6, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking7': {'Vaga': 7, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking8': {'Vaga': 8, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking9': {'Vaga': 9, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking10': {'Vaga': 10, 'Status': 'Livre',
                          'Carro': None, 'Placa': None},
        }
        self.money = 0
        self.entrada = 0

    def adicionar_carro(self, carro, placa=None):
        placa = gerador()
        self.carro = carro
        self.placa = placa

        if self.carro in lista_de_carros:
            for x in range(1, len(self.vaga)+1):

                if self.vaga[f'parking{x}']['Status'] == 'Livre':
                    self.vaga[f'parking{x}']['Status'] = 'Ocupado'
                    self.vaga[f'parking{x}']['Carro'] = self.carro
                    self.vaga[f'parking{x}']['Placa'] = self.placa
                    print(
                        f"\033[32m{'A vaga ':->20}{x}{' foi ocupada':-<19}\033[m")
                    x = len(self.vaga)
                    self.money += 10.0
                    self.entrada += 1
                    break
            else:
                print(
                    f'\033[31m{"Todas as vagas estão ocupadas":-^40}\033[m')
                sleep(0.5)
        else:
            print(
                f'\033[31m{"Nome de carro invalido":-^40}\033[m')
            sleep(1)

    def vagas(self):
        a = 1
        while a <= len(self.vaga):
            for x, y in self.vaga[f'parking{a}'].items():
                print(f"{x}-\033[35m{y}\033[m")
            print()
            a += 1
        else:
            sleep(2)

    def remover_carro(self, vaga=0):
        for x in range(1, len(self.vaga)+1):
            if self.vaga[f'parking{x}']['Status'] == 'Ocupado':
                self.vagas()
                sleep(2)
                remover = str(
                    input('Digite o nome da vaga que você quer remover o carro: '))
                if remover:
                    self.vaga[f'parking{remover}']['Status'] = 'Livre'
                    self.vaga[f'parking{remover}']['Carro'] = None
                    self.vaga[f'parking{remover}']['Placa'] = None
                    print(
                        f"\033[32m{'Vaga ':->20}{remover}{' liberada':-<19}\033[m")
                    break
        else:
            print(
                f'\033[32m{"Todas as vagas estão Livres!":-^40}\033[m')

    def liberar(self):
        for x in range(1, len(self.vaga)+1):
            self.vaga[f'parking{x}']['Status'] = 'Livre'
            self.vaga[f'parking{x}']['Carro'] = None
            self.vaga[f'parking{x}']['Placa'] = None
        print(f'{"Todas as vagas foram liberadas!":-^40}')

    def relatorio(self):
        if self.money == 0:
            print(f'\033[31m{"Não a dinheiro no caixa":-^40}\033[m')
        else:
            date = datetime.now()
            print(
                f'\033[32m{"Relatório de estacionamento":-^40}\033[m\n'

                f'\n\033[1m-Data e hora atual: {date.strftime("%d/%m/%Y - %H:%M:%S")}\033[m\n'

                f'\033[1m-Total de dinheiro recebido: R${self.money}\033[m\n'

                f'\033[1m-Total de carros estacionados: {self.entrada}\033[m\n')


teste = estacionamento()
