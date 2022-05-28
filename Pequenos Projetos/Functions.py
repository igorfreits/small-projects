class Cart:

    def __init__(self) -> None:
        self.purchases = {}  # carrinho de compras

    def insect_products(self, compras, price):  # adiciona itens e preços no carrinho
        if 'Cart Items' not in self.purchases:
            self.purchases['Cart Items'] = {compras: 'R$'+price}
        else:
            self.purchases['Cart Items'].update({compras: 'R$'+price})

    def list_cart(self):  # mostra os itens do carrinho enumerados
        carrinho = pay.purchases['Cart Items']
        for a, (b, c) in enumerate(carrinho.items()):
            print(f'\033[34m Item Code {a} - {b} = R${c}\033[m')

        print(
            # itens do carrinho
            f'O seu carrinho contem {len(pay.purchases["Cart Items"])}'
            f'e ele tem um valor total de: R${total}')  # valor total do carrinho


total = 0  # valor total
pay = Cart()  # Chama a classe Cart
