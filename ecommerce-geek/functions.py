from random import randint
from datetime import datetime


class Cart:
    print(f'{"Geek Commerce":-^40}')

    def __init__(self):
        self.purchases = {}  # carrinho de compras{Produto:valor}

    def insect_products(self, compras, price):
        # adiciona itens e preços no carrinho
        if 'Cart Items' not in self.purchases:
            self.purchases['Cart Items'] = {compras: int(price)}
        else:
            self.purchases['Cart Items'].update({compras: int(price)})

    def list_cart(self):  # mostra os itens do carrinho enumerados
        carrinho = self.purchases['Cart Items']

        for a, (b, c) in enumerate(carrinho.items()):
            print(f'\033[34m Item Code {a} - {b} = R${c}\033[m')

        print(
            # itens do carrinho
            f'O seu carrinho contem \033[32m{len(self.purchases["Cart Items"])}\033[m itens'
            f' e ele tem um valor total de: \033[32mR${sum_total(self)}\033[m')  # valor total do carrinho

    def payment(self):  # Pagamento em dinheiro e credito
        payment = int(input(f'Valor total do carrinho: \033[32mR${sum_total(self)}\033[m'
                            '\nEscolha a forma de pagamento: '
                            '\n [ 1 ] - A vista no debito/cartão ou Pix - 10% de desconto'
                            '\n [ 2 ] - Cartão de credito - Juros a partir de 5x pra cima'
                            '\n ...'))
        match payment:
            case 1:
                money = int(input('Pagamento em dinheiro foi selecionado'
                                  '\n Digite o valor que ira pagar: '))
                if money < sum_total(self):
                    print(
                        '\033[31mVoce nao tem dinheiro suficiente, selecione outra opção de pagamento\033[m')
                    self.payment()

                elif money == sum_total(self):
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')

                elif money > sum_total(self):
                    a = money - sum_total(self)
                    print(
                        f'voce nos deu {money:.2f} e seu troco e de {a}')
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                    note(self)
                else:
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                    note(self)

            case 2:
                credit = int(input('Em quantas vezes voce quer parcela? '))
                print(
                    f'A sua compra tem um total de R${sum_total(self)} e sera parcelado em X{credit}')

                if credit < 3:  # 5% de desconto
                    print(
                        f'Voce recebeu \033[35m5%\033[m de desconto e agora sua compra tera um valor total de:'
                        f'\033[35m R${sum_total(self)-(sum_total(self) * 5 / 100)} \033[m\n'
                        f'\nE a parcela de sua compra sera de: \033[35mR${(sum_total(self)-sum_total(self) * 5 / 100)/credit:.2f}\033[m'
                        '\n\033[34mO seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                    note(self)

                elif credit <= 7:  # 5% de juros
                    print(f'Sera cobrado \033[35m5%\033[m de juros e agora sua compra tem o valor total de'
                          f'\033[35m R${sum_total(self)+(sum_total(self) * 5 / 100 )} \033[m'
                          f'\nE a parcela de sua compra sera de: \033[35mR${(sum_total(self)+sum_total(self) * 5 / 100)/credit:.2f}\033[m'
                          '\n\033[34mO seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                    note(self)

                elif credit >= 10:  # 10% de juros
                    print(f'Sera cobrado \033[35m10%\033[m de juros e agora sua compra tem o valor total de'
                          f'\033[35m R${sum_total(self)+(sum_total(self) * 10 / 100 )} \033[m'
                          f'\nE a parcela de sua compra sera de: \033[35mR${(sum_total(self)-sum_total(self) * 10 / 100)/credit:.2f}\033[m'
                          '\n\033[34mO seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                    note(self)


def note(self):
    # emissão da nota fiscal
    z = self.purchases['Cart Items']
    with open('note.txt', 'w+')as file:
        file.write(f'{"Geek Commerce":-^40}'
                   f'\n {"Cupom fiscal":-^40}'
                   # Código gerado aleatoriamente
                   f'\nCODE {randint(0,100)} - '
                   # Data atual, hora atual
                   f'{datetime.today().strftime("%d/%m/%Y - %H:%M:%S")}\n')
        for a, (b, c) in enumerate(z.items()):
            file.write(f'\nItem Code {a} - {b} = R${c}')
        file.write(f'\nTotal: {sum_total(self)}')


def sum_total(self):  # Valor total do carrinho
    carrinho = self.purchases['Cart Items']
    total = 0
    total = sum(map(lambda
                    carrinho: float(carrinho), carrinho.values()))
    return total


pay = Cart()  # Chama a classe Cart
