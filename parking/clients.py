from typing import List
from data import board_generate, cpf_generate
from data import car_list, id
from functions import parking
import json


class Registration:
    def __init__(self):
        self.name = None
        self.cpf = None
        self.id = None
        self.car = None
        self.board = None
        self.registers: List = []

    def new_register(self):
        self.name = str(input('enter your name: ')).upper().strip()
        self.registers.append(self.name)
        self.cpf = cpf_generate()
        self.id = id()
        self.board = board_generate()

        car = str(input('what is the name of your car: ')).upper().strip()
        if car in car_list:
            self.car = car
            self.save()
            return self.registers
        else:
            print(
                f'\033[31m{"invalid car name!":-^40}\033[m')
            self.new_register()

    def report_clients(self):
        print(f'\033[34m{"Customer report":-^40}\033[m')
        print()

        print(f'\033[31m{"New clients":-^40}\033[m')
        for new in self.registers:
            print(new)

        print()

        print(
            f'\033[32m-We had a total of {len(self.registers)} new registrations!\033[m')

        print()

        with open('data/clients.json', 'r') as f:
            clients = json.load(f)
            for x, y in clients.items():
                print(f'{x, y}')

    def save(self):
        try:
            with open('data/clients.json', 'r') as f:
                clients = json.load(f)
        except FileNotFoundError:
            clients = {}

        clients[self.id] = {
            'name': self.name,
            'CPF': self.cpf,
            'car': self.car,
            'board': self.board}

        with open('data/clients.json', 'w') as f:
            json.dump(clients, f, indent=4)

        print(
            f'\033[32m{"Client registered successfully":-^40}\033[m')
        print(f'{"O seu ID é:":->20} {self.id:-<20}')


class User(Registration):
    def __init__(self):
        Registration.__init__(self)

    def login(self):
        name = input('Enter your name: ').upper().strip()
        code = input('Enter your ID: ')

        with open('data/clients.json', 'r') as f:
            clients = json.load(f)

        if code in clients:
            print(f'\033[32m{"Welcome":->20} {name:-<20}\033[m')
            parking.add_car(
                clients[code]['name'], clients[code]['CPF'],
                clients[code]['car'], clients[code]['board'],
                code)

        else:
            print(f'\033[31m{"User not registered":-^40}\033[m')


register = Registration()
user = User()
