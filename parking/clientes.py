from abc import ABC, abstractmethod
from data import placa_generate, cpf_generate
from data import lista_de_carros, id
from functions import parking
import json


class Clientes(ABC):
    @abstractmethod
    def novo_cadastro(self):
        pass


class Cadastro(Clientes):
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.id = None
        self.carro = None
        self.placa = None
        self.new_register = 0
        self.registers = []

    def novo_cadastro(self):
        self.nome = str(input('Digite seu nome: ')).upper().strip()
        self.cpf = cpf_generate()
        self.id = id()
        self.placa = placa_generate()
        self.registers.append(self.nome)

        car = str(input('Digite seu carro: ')).upper().strip()
        if car in lista_de_carros:
            self.carro = car
        else:
            print(
                f'\033[31m{"Nome de carro invalido":-^40}\033[m')
            self.novo_cadastro()
            self.new_register += 1

        self.save()

    def save(self):
        # tratar o erro JSONDecodeError
        try:
            with open('data/clientes.json', 'r') as f:
                clientes = json.load(f)
        except FileNotFoundError:
            clientes = {}
        clientes[self.id] = {
            'Nome': self.nome,
            'CPF': self.cpf,
            'Carro': self.carro,
            'Placa': self.placa}

        with open('data/clientes.json', 'w') as f:
            json.dump(clientes, f, indent=4)

        print(
            f'\033[32m{"Cliente cadastrado com sucesso":-^40}\033[m')
        print(f'{"O seu ID é:":->20} {self.id:-<20}')
        self.new_register += 1


class Usuario(Cadastro):
    def __init__(self):
        Cadastro.__init__(self)

    def login(self):
        nome = input('Digite seu nome: ').upper().strip()
        codigo = input('Digite seu ID: ')

        with open('data/clientes.json', 'r') as f:
            clientes = json.load(f)

        if codigo and nome in clientes:
            print(f'\033[32m{"Bem vindo":->20} {nome:-<20}\033[m')
            parking.adicionar_carro(
                clientes[codigo]['Nome'], clientes[codigo]['CPF'],
                clientes[codigo]['Carro'], clientes[codigo]['Placa'],
                codigo)

        else:
            print(f'\033[31m{"Usuário não cadastrado":-^40}\033[m')

    def relatorio_clientes(self):
        print(f'\033[34m{"Relatório de clientes":-^40}\033[m')
        print()

        print(f'\033[31m{"Novos clientes":-^40}\033[m')
        for new in self.registers:
            print(f'-{new}')
        print()

        print(
            f'\033[32m-Tivemos um total de {self.new_register} novos cadastros!\033[m')

        print()

        with open('data/clientes.json', 'r') as f:
            clientes = json.load(f)
            for x, y in clientes.items():
                print(f'-{x, y}')


register = Cadastro()
user = Usuario()
