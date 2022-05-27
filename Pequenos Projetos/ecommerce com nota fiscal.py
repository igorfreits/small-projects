print(f'{"Geek Commerce":-^40}')


# funções
def produto():  # Adiciona os produtos no carrinho
    carrinho.append(compras)


carrinho = []
total = 0

while True:
    options = int(input('Seja bem-vindo a Geek Commerce'
                        '\n Como podemos te ajudar? '
                        '\n [ 1 ] - Produtos'
                        '\n [ 2 ] - Ir para o carrinho'
                        '\n [ 3 ] - Pagamento'
                        '\n ...'))
    match options:
        case 1:
            compras = str(
                input('Qual item voce deseja comprar? ')).upper().strip()
            print(
                f'O item \033[35m"{compras}"\033[m foi adicionado ao seu carrinho de compras')
            produto()
        case 2:
            print('\033[31m O seu carrinho nao tem nenhum item!\033[m') if len(carrinho) == 0 else print(f'O seu carrinho tem os seguintes items:'
                                                                                                         f'\n \033[35m{carrinho}\033[m')
        case 3:
            payment = int(input('Escolha a forma de pagamento:'
                                '\n [ 1 ] - A vista no debito/cartão ou Pix - 10% de desconto'
                                '\n [ 2 ] - Cartão de credito - Juros a partir de 5x e 10x'))
            if payment == 1:
                debito = total - (total*10/100)
                print(debito)
