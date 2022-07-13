from functions import pay
while True:
    options1 = int(input('Seja bem-vindo a Geek Commerce'
                             '\n Como podemos te ajudar? '
                             '\n [ 1 ] - Comprar'
                             '\n [ 2 ] - Ir para o carrinho'
                             '\n [ 3 ] - Pagamento'
                             '\n ...'))
    match options1:
        case 1:
                compras = input(
                    'Qual item voce deseja comprar? ').upper().strip()
                price = int(input('Qual o valor do produto? '))
                print(
                    f'O item \033[35m"{compras}"\033[m foi adicionado ao seu carrinho de compras e tem o valor de \033[35mR${price}\033[m')
                pay.insect_products(compras, price)

        case 2:
            if len(pay.purchases) == 0:
                    print('\033[31m O seu carrinho nao tem nenhum item!\033[m')
            else:
                    pay.list_cart()
                    options2 = int(input('Oque voce deseja fazer agora?'
                                         '\n [ 1 ] - pagamento'
                                         '\n [ 2 ] - voltar'
                                         '\n ...'))
                if options2 == 1:
                        pay.payment()
                        break
                elif options2 == 2:
                        continue

        case 3:
            if len(pay.purchases) == 0:
                    print('\033[31m O seu carrinho nao tem nenhum item!\033[m')
            else:
                    pay.payment()
                    break
