class estacionamento:
    def __init__(self, carro, placa):
        self.carro = carro
        self.placa = placa
        parking = {'Vagas': int, 'Status': str, 'Carro': str, 'Placa': str}

    def adicionar_carro(self):
        pass


if __name__ == '__main__':
    a = estacionamento('celta', 'ABC-1234')
    a.adicionar_carro()
