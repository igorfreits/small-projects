from data import lista_de_carros, gerador
from time import sleep


class estacionamento:
    def __init__(self):

        self.a1 = {'Vaga': 1, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a2 = {'Vaga': 2, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a3 = {'Vaga': 3, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

    def adicionar_carro(self, carro, placa=None):
        placa = gerador()
        self.carro = carro
        self.placa = placa

        if self.carro in lista_de_carros:

            if 'Ocupado' in self.a1['Status'] and 'Ocupado' in self.a2['Status']:
                if self.a3['Status'] == 'Livre':
                    self.a3['Carro'] = self.carro
                    self.a3['Placa'] = self.placa
                    self.a3['Status'] = 'Ocupado'
                    print(
                        f'\033[32m{"Seu carro foi adicionado na vaga 3":-^40}'
                        '\033[m')
                else:
                    print(f'\033[31m{"Estacionamento lotado!":-^40}\033[m')

            if self.a1['Status'] == 'Livre':
                self.a1['Carro'] = self.carro
                self.a1['Placa'] = self.placa
                self.a1['Status'] = 'Ocupado'
                print(
                    f'\033[32m{"Seu carro foi adicionado na vaga 1":-^40}'
                    '\033[m')

            elif 'Ocupado' in self.a1['Status']:
                if self.a2['Status'] == 'Livre':
                    self.a2['Carro'] = self.carro
                    self.a2['Placa'] = self.placa
                    self.a2['Status'] = 'Ocupado'
                    print(
                        f'\033[32m{"Seu carro foi adicionado na vaga 2":-^40}'
                        '\033[m')

        else:
            print(f'\033[31m{"Nome de carro invalido":-^40}\033[m')
            sleep(1)

    def vagas(self):
        for x, y in self.a1.items():
            print(f'{x}-\033[35m{y}\033[m')
        print()

        for x, y in self.a2.items():
            print(f'{x}-\033[36m{y}\033[m')
        print()

        for x, y in self.a3.items():
            print(f'{x}-\033[33m{y}\033[m ')
        print()
        sleep(3)

    def remover_carro(self, vaga=0):
        self.vagas()
        sleep(1)
        vaga = int(
            input('Digite o nome da vaga que você quer remover o carro: '))

        if vaga == 1:
            self.a1['Status'] = 'Livre'
            self.a1['Carro'] = None
            self.a1['Placa'] = None
            print(f'\033[32m{"Vaga 1 liberada":-^40}\033[m')
        if vaga == 2:
            self.a2['Status'] = 'Livre'
            self.a2['Carro'] = None
            self.a2['Placa'] = None
            print(f'\033[32m{"Vaga 2 liberada":-^40}\033[m')
        if vaga == 3:
            self.a3['Status'] = 'Livre'
            self.a3['Carro'] = None
            self.a3['Placa'] = None
            print(f'\033[32m{"Vaga 3 liberada":-^40}\033[m')

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

        print(f'{"Todas as vagas foram liberadas!":-^40}')

    def relatorio(self):
        print(f'{"Finge que aparece vários gráficos aqui":-^40}')


teste = estacionamento()
