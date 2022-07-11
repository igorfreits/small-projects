from data import lista_de_carros, c
from time import sleep


class estacionamento:
    def __init__(self):

        self.a1 = {'Vaga': 1, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a2 = {'Vaga': 2, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

        self.a3 = {'Vaga': 3, 'Status': 'Livre',
                   'Carro': None, 'Placa': None}

    def adicionar_carro(self, carro, placa=c):
        self.carro = carro
        self.placa = placa
        if self.carro in lista_de_carros:

            if 'Ocupado' in self.a1['Status'] and 'Ocupado' in self.a2['Status']:
                if self.a3['Status'] == 'Livre':
                    self.a3['Carro'] = self.carro
                    self.a3['Placa'] = self.placa
                    self.a3['Status'] = 'Ocupado'
                    print(
                        '\033[32mSeu carro foi adicionado na vaga 3\033[m')
                else:
                    print('\033[31mEstacionamento lotado!\033[m')

            if self.a1['Status'] == 'Livre':
                self.a1['Carro'] = self.carro
                self.a1['Placa'] = self.placa
                self.a1['Status'] = 'Ocupado'
                print('\033[32mSeu carro foi adicionado na vaga 1\033[m')

            elif 'Ocupado' in self.a1['Status']:
                if self.a2['Status'] == 'Livre':
                    self.a2['Carro'] = self.carro
                    self.a2['Placa'] = self.placa
                    self.a2['Status'] = 'Ocupado'
                    print('\033[32mSeu carro foi adicionado na vaga 2\033[m')

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
        print('Finge que aparece varios graficos aqui')


teste = estacionamento()
