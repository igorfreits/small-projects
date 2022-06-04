class Cart:
    def __init__(self):
        self.purchases = {}  # carrinho de compras

    # adiciona itens e preços no carrinho

    def insect_products(self, compras, price):
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

    def payment(self):
        payment = int(input('Escolha a forma de pagamento:'
                            '\n [ 1 ] - A vista no debito/cartão ou Pix - 10% de desconto'
                            '\n [ 2 ] - Cartão de credito - Juros a partir de 5x pra cima'
                            '\n ...'))
        match payment:
            case 1:
                money = int(input('Pagamento em dinheiro foi selecionado'
                                  '\n Digite o valor que ira pagar: '))
                if money < sum_total():
                    print(
                        'Voce nao tem dinheiro suficiente, selecione outra opção de pagamento')
                    self.payment()

                elif money == sum_total():
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')

                elif money > sum_total(self):
                    a = money - sum_total(self)
                    print(
                        f'voce nos deu {money:.2f} e seu troco e de {a}')
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
                else:
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')
            case 2:
                credit = int(input('Em quantas vezes voce quer parcela? '))
                print(
                    f'A sua compra tem um total de R${sum_total(self)} e sera parcelado em X{credit}')

                if credit < 3:  # 5% de desconto
                    print(
                        f'Voce recebeu \033[35m 5% \033[m de desconto e agora sua compra tera um valor total de:'
                        f'\033[35m R${sum_total(self)-(sum_total(self) * 5 / 100)} \033[m')
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')

                elif credit >= 7:  # 5% de juros
                    print(f'Sera cobrado \033[35m 5% \033[m de juros e agora sua compra tem o valor total de'
                          f'\033[35m R${sum_total(self)+(sum_total(self) * 5 / 100 )} \033[m')
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce!\033[m')

                elif credit > 10:  # 10% de juros
                    print(f'Sera cobrado \033[35m 10% \033[m de juros e agora sua compra tem o valor total de'
                          f'\033[35m R${sum_total(self)+(sum_total(self) * 10 / 100 )} \033[m')
                    print(
                        '\033[34m O seu pagamento foi um sucesso, obrigado pro comprar na "Geek Commerce"!\033[m')


def sum_total(self):
    carrinho = self.purchases['Cart Items']
    total = 0
    total = sum(map(lambda
                    carrinho: float(carrinho), carrinho.values()))
    return total


pay = Cart()  # Chama a classe Cart
