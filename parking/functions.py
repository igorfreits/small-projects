import matplotlib.pyplot as plt
from time import sleep
from datetime import datetime, timedelta
from random import randint
import json


class Parking:
    def __init__(self):

        self.vacancy = {
            'parking1': {'vacancy': 1, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking2': {'vacancy': 2, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking3': {'vacancy': 3, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking4': {'vacancy': 4, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking5': {'vacancy': 5, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking6': {'vacancy': 6, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking7': {'vacancy': 7, 'name': None, 'CPF': None,
                         'ID': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking8': {'vacancy': 8, 'name': None, 'CPF': None,
                         'Id': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking9': {'vacancy': 9, 'name': None, 'CPF': None,
                         'Id': None, 'Status': 'free',
                         'car': None, 'board': None,
                         'entry': None},
            'parking10': {'vacancy': 10, 'name': None, 'CPF': None,
                          'Id': None, 'Status': 'free',
                          'car': None, 'board': None,
                          'entry': None}
        }
        self.money = 0
        self.entry = 0

    def add_car(self, name, cpf, car, board, code):

        self.name = name
        self.car = car
        self.board = board
        self.cpf = cpf
        self.id = code

        data = datetime.now()

        for x in range(1, len(self.vacancy)+1):
            if self.vacancy[f'parking{x}']['Status'] == 'free':
                self.vacancy[f'parking{x}']['Status'] = 'occupied'
                self.vacancy[f'parking{x}']['name'] = self.name
                self.vacancy[f'parking{x}']['car'] = self.car
                self.vacancy[f'parking{x}']['board'] = self.board
                self.vacancy[f'parking{x}']['CPF'] = self.cpf
                self.vacancy[f'parking{x}']['ID'] = self.id
                self.vacancy[f'parking{x}']['entry'] = data

                print(
                    f"\033[32m{'vacancy ':->20}{x}{' has been occupied':-<19}\033[m")
                self.entry += 1
                break
        else:
            print(
                f'\033[31m{"All vacancies are occupied":-^40}\033[m')
            sleep(0.5)

    def vacancys(self):
        a = 1
        while a <= len(self.vacancy):
            for x, y in self.vacancy[f'parking{a}'].items():
                print(f"{x}-\033[35m{y}\033[m")
            print()
            a += 1
        else:
            sleep(1)

    def remove_car(self, vacancy=0):
        for x in range(1, len(self.vacancy)+1):
            if self.vacancy[f'parking{x}']['Status'] == 'occupied':
                self.vacancys()
                sleep(1)

                remove = str(
                    input('Enter the name of the vacancy you want to remove the car: '))
                if remove:
                    self.vacancy[f'parking{remove}']['Status'] = 'free'
                    self.vacancy[f'parking{remove}']['car'] = None
                    self.vacancy[f'parking{remove}']['board'] = None
                    self.vacancy[f'parking{remove}']['name'] = None
                    self.vacancy[f'parking{remove}']['CPF'] = None
                    self.vacancy[f'parking{remove}']['ID'] = None

                    entry = self.vacancy[f'parking{remove}']['entry']

                    exit = entry + \
                        timedelta(minutes=randint(10, 180))

                    difference = exit - \
                        entry

                    time = difference.seconds // 60

                    if time <= 30:
                        print(
                            f'\033[31mYou stayed {time} minutes and will have to pay R$7\033[m')
                        self.money += 7
                    elif time <= 60:
                        print(
                            f'\033[31mYou stayed {time} minutes and will have to pay R$15\033[m')
                        self.money += 15
                    elif time <= 90:
                        print(
                            f'\033[31mYou stayed {time} minutes and will have to pay R$25\033[m')
                        self.money += 30
                    elif time >= 120:
                        print(
                            f'\033[31mYou stayed {time} minutes and will have to pay R$35\033[m')
                        self.money += 35

                    self.vacancy[f'parking{remove}']['entry'] = None

                    print(
                        f"\033[32m{'vacancy ':->20}{remove}{'released':-<19}\033[m")
                    break
        else:
            print(
                f'\033[32m{"All vacancies are free!":-^40}\033[m')

    def reports(self):
        date = datetime.now()
        print(
            f'\033[32m{"Parking report":-^40}\033[m\n'

            f'\n\033[1m-Current date and time: {date.strftime("%d/%m/%Y - %H:%M:%S")}\033[m\n'

            f'\033[1m-Total money received: BRL{self.money}\033[m\n'

            f'\033[1m-Total parked cars: {self.entry}\033[m\n')
        try:
            with open('data/report.json', 'r') as f:
                report = json.load(f)
        except FileNotFoundError:
            report = {}
        date = datetime.now()
        months_in_full = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                          5: 'May', 6: 'June', 7: 'July', 8: 'August',
                          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

        for x, y in months_in_full.items():
            if date.month == x:
                break

        report[y] = {
            'Cashier': self.money}

        with open('data/report.json', 'w') as f:
            json.dump(report, f, indent=4)

        with open('data/report.json', 'r') as f:
            report = json.load(f)

        data = []
        cashier = []
        for x in report:
            data.append(x)
            cashier.append(report[x]['Cashier'])

        plt.bar(data, cashier)
        plt.title('Parking Monthly Cashier')
        plt.bar(data, cashier, color=[
                '#3299CC', '#00FF00', '#228B22', '#FFFF00',
                '#00FFFF', '#FF00FF'], edgecolor='black')
        plt.xlabel('2022')
        plt.ylabel('Valores R$')
        plt.show()


parking = Parking()
