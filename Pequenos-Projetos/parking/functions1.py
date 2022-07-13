from data import lista_de_carros, gerador
from time import sleep


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

    def adicionar_carro(self, carro, placa=None):
        placa = gerador()
        self.carro = carro
        self.placa = placa

        x = 1
        while True or x <= len(self.vaga):
            if self.vaga[f'parking{x}']['Status'] == 'Ocupado':
                x += 1
                if x == 10:
                    print(
                        f'\033[31m{"Estacionamento lotado":-^40}\033[m')
                    x = 1
                    break

            else:
                if self.carro in lista_de_carros:
                    self.vagas()
                    sleep(2)
                adicionar = str(
                    input('Digite o numero da vaga que você deseja estacionar: '))

                if self.vaga[f'parking{adicionar}']['Status'] == 'Ocupado':
                    print(
                        f'\033[31m{"Esta vaga esta ocupada, Selecione outra!":-^40}\033[m')

                if adicionar:
                    self.vaga[f'parking{adicionar}']['Status'] = 'Ocupado'
                    self.vaga[f'parking{adicionar}']['Carro'] = self.carro
                    self.vaga[f'parking{adicionar}']['Placa'] = self.placa
                    print(
                        f"\033[32m{'Você estacionou na vaga: ':->20}{adicionar}{'':-<19}\033[m")
                else:
                    x = 1
                    print(
                        f'\033[31m{"Nome de carro invalido":-^40}\033[m')
                    sleep(1)
                    break

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
        x = 1
        while True or x <= len(self.vaga):
            if self.vaga[f'parking{x}']['Status'] == 'Livre':
                x += 1
                if x == 10:
                    print(
                        f'\033[31m{"Todas as vagas estão disponíveis":-^40}\033[m')
                    sleep(0.5)
                    x = 1
                    break

            else:
                x = 1
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

    def liberar(self):
        a = 1
        while a <= len(self.vaga):
            self.vaga[f'parking{a}']['Status'] = 'Livre'
            self.vaga[f'parking{a}']['Carro'] = None
            self.vaga[f'parking{a}']['Placa'] = None
            a += 1
        print(f'{"Todas as vagas foram liberadas!":-^40}')

    def relatorio(self):
        print(f'{"Finge que aparece vários gráficos aqui":-^40}')


teste = estacionamento()
