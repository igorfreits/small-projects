class Cart:

    def __init__(self) -> None:
        self.purchases = {}  # carrinho de compras

    def insect_products(self, compras, price):  # adiciona itens e preços no carrinho
        if 'Cart Items' not in self.purchases:
            self.purchases['Cart Items'] = {compras: int(price)}
        else:
            self.purchases['Cart Items'].update({compras: int(price)})

    def list_cart(self):  # mostra os itens do carrinho enumerados
        carrinho = self.purchases['Cart Items']
        total = 0
        total = sum(map(lambda
                        carrinho: float(carrinho), carrinho.values()))
        for a, (b, c) in enumerate(carrinho.items()):
            print(f'\033[34m Item Code {a} - {b} = R${c}\033[m')

        print(
            # itens do carrinho
            f'O seu carrinho contem \033[32m{len(self.purchases["Cart Items"])}\033[m itens'
            f' e ele tem um valor total de: \033[32mR${total}\033[m')  # valor total do carrinho


pay = Cart()  # Chama a classe Cart
