from Functions import pay  # importa o arquivo Function que contem as classes e funções
print(f'{"Geek Commerce":-^40}')

while True:
    options = int(input('Seja bem-vindo a Geek Commerce'
                        '\n Como podemos te ajudar? '
                        '\n [ 1 ] - Produtos'
                        '\n [ 2 ] - Ir para o carrinho'
                        '\n [ 3 ] - Pagamento'
                        '\n ...'))
    match options:
        case 1:
            compras = input('Qual item voce deseja comprar? ').upper().strip()
            price = int(input('Qual o valor do produto? '))

            print(
                f'O item \033[35m"{compras}"\033[m foi adicionado ao seu carrinho de compras e tem o valor de \033[35mR${price}\033[m')
            pay.insect_products(compras, price)
        case 2:
            if len(pay.purchases) == 0:
                print('\033[31m O seu carrinho nao tem nenhum item!\033[m')
            else:
                pay.list_cart()

        case 3:
            if len(pay.purchases) == 0:
                print('\033[31m O seu carrinho nao tem nenhum item!\033[m')
            else:
                payment = int(input('Escolha a forma de pagamento:'
                                    '\n [ 1 ] - A vista no debito/cartão ou Pix - 10% de desconto'
                                    '\n [ 2 ] - Cartão de credito - Juros a partir de 5x e 10x'))
