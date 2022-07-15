from abc import ABC, abstractmethod
from data import placa_generate, cpf_generate, telefone_generate, lista_de_carros
import json
from functions import a


class Clientes(ABC):
    @abstractmethod
    def novo_cadastro(self):
        pass


class Cadastro(Clientes):
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.endereco = None
        self.telefone = None
        self.carro = None
        self.placa = None

    def novo_cadastro(self):
        self.nome = str(input('Digite seu nome: ')).upper().strip()
        self.cpf = cpf_generate()
        self.telefone = telefone_generate()

        car = str(input('Digite seu carro: ')).upper().strip()
        if car in lista_de_carros:
            self.carro = car
        else:
            print(
                f'\033[31m{"Nome de carro invalido":-^40}\033[m')

        self.placa = placa_generate()
        self.new = 0

        for x in range(50):
            dados = {f'User{x}':
                     {'Nome': "",
                      'CPF': "",
                      'Telefone': "",
                      'Carro': "",
                      'Placa': "",
                      'Status': "Offline"}, }

            with open('data.json', 'a') as f:
                json.dump(dados, f, indent=4)

            with open('data.json', '') as f:
                a = json.load(f)
                if a[f'User{x}']['Status'] == "Offline":
                    a[f'User{x}']['Nome'] = self.nome
                    a[f'User{x}']['CPF'] = self.cpf
                    a[f'User{x}']['Telefone'] = self.telefone
                    a[f'User{x}']['Carro'] = self.carro
                    a[f'User{x}']['Placa'] = self.placa
                    a[f'User{x}']['Status'] = "Online"
                    json.dump(a, f, indent=4)

                self.new += 1
                print(
                    f'\033[32m{"Cadastro realizado com sucesso":-^40}\033[m')
                break


class Usuario(Cadastro):
    def __init__(self):
        Cadastro.__init__(self)

    def verifica(self):
        nome = str(input('Digite seu nome: '))
        cpf = str(input('Digite seu CPF: '))
        self.nome = nome
        self.cpf = cpf

        # verifica se o cliente existe no arquivo json
        with open('data.json', 'r') as arquivo:
            for x in arquivo:
                if x == self.cpf:
                    print(f'\033[32m{"Cliente existe":-^40}\033[m')
                    break
            else:
                print(f'\033[31m{"Cliente não existe":-^40}\033[m')

    def relatorio_clientes(self):
        print(f'\033[34m{"Relatório de clientes":-^40}\033[m')

        with open('data.json', 'w+') as arquivo:
            for x in arquivo:
                print(x)


register = Cadastro()
user = Usuario()
