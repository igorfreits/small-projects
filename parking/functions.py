from data import lista_de_carros, placa_generate, cpf_generate, id
from time import sleep
from datetime import datetime


class estacionamento:
    def __init__(self):

        self.vaga = {
            'parking1': {'Vaga': 1, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None, 'Saida': None},
            'parking2': {'Vaga': 2, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            'parking3': {'Vaga': 3, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None},
            # 'parking4': {'Vaga': 4, 'Nome': None, 'CPF': None,
            #              'ID': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking5': {'Vaga': 5, 'Nome': None, 'CPF': None,
            #              'ID': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking6': {'Vaga': 6, 'Nome': None, 'CPF': None,
            #              'ID': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking7': {'Vaga': 7, 'Nome': None, 'CPF': None,
            #              'ID': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking8': {'Vaga': 8, 'Nome': None, 'CPF': None,
            #              'Id': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking9': {'Vaga': 9, 'Nome': None, 'CPF': None,
            #              'Id': None, 'Status': 'Livre',
            #              'Carro': None, 'Placa': None},
            # 'parking10': {'Vaga': 10, 'Nome': None, 'CPF': None,
            #               'Id': None, 'Status': 'Livre',
            #               'Carro': None, 'Placa': None}


        }
        self.money = 0
        self.entrada = 0

    def adicionar_carro(self, nome, cpf, carro, placa, codigo):

        self.nome = nome
        self.carro = carro
        self.placa = placa
        self.cpf = cpf
        self.id = codigo

        for x in range(1, len(self.vaga)+1):
            if self.vaga[f'parking{x}']['Status'] == 'Livre':
                self.vaga[f'parking{x}']['Status'] = 'Ocupado'
                self.vaga[f'parking{x}']['Nome'] = self.nome
                self.vaga[f'parking{x}']['Carro'] = self.carro
                self.vaga[f'parking{x}']['Placa'] = self.placa
                self.vaga[f'parking{x}']['CPF'] = self.cpf
                self.vaga[f'parking{x}']['ID'] = self.id

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
                    self.vaga[f'parking{remover}']['Nome'] = None
                    self.vaga[f'parking{remover}']['CPF'] = None
                    self.vaga[f'parking{remover}']['ID'] = None
                    print(
                        f"\033[32m{'Vaga ':->20}{remover}{' liberada':-<19}\033[m")
                    break
        else:
            print(
                f'\033[32m{"Todas as vagas estão Livres!":-^40}\033[m')

    def liberar(self):
        for x in range(1, len(self.vaga)+1):
            self.vaga[f'parking{x}']['Status'] = 'Livre'
            self.vaga[f'parking{x}']['Nome'] = None
            self.vaga[f'parking{x}']['Carro'] = None
            self.vaga[f'parking{x}']['Placa'] = None
            self.vaga[f'parking{x}']['CPF'] = None
            self.vaga[f'parking{x}']['ID'] = None
        print(f'{"Todas as vagas foram liberadas!":-^40}')

    def relatorio_parking(self):
        if self.money == 0:
            print(f'\033[31m{"Não a dinheiro no caixa":-^40}\033[m')
        else:
            date = datetime.now()
            print(
                f'\033[32m{"Relatório de estacionamento":-^40}\033[m\n'

                f'\n\033[1m-Data e hora atual: {date.strftime("%d/%m/%Y - %H:%M:%S")}\033[m\n'

                f'\033[1m-Total de dinheiro recebido: R${self.money}\033[m\n'

                f'\033[1m-Total de carros estacionados: {self.entrada}\033[m\n')


parking = estacionamento()
