from data import emoji1, emoji2, emoji3, emoji4, emoji5, emoji6, emoji7, emoji8, emoji9, emoji10
from functions import parking
from clientes import register, user


while True:
    option = int(input(f'\033[34m{"BEM VINDO AO PARKING ISTOP":-^40}'"\n"
                       f'{"Menu inicial":-^40}\033[m'

                       f'\n1 -{emoji2}  Entrar ou criar um novo cadastro'
                       f'\033[31m \n2 -{emoji6}   Remover veiculo \033[m'
                       f'\033[34m \n3 -{emoji1}   Vagas \033[m'
                       f'\n4 -{emoji3}  Relatório'
                       f'\n5 -{emoji4}  Liberar todos as vagas'
                       f'\033[32m \n6 -{emoji5}  Sair \033[m'

                       f'\n\n-Digite a opção desejada: '))
    match option:
        case 1:
            option = int(input('Escolha uma opção: \n'
                         f'\033[35m\n1 -{emoji7} Entrar no estacionamento\033[m'
                               f'\n2 -{emoji8} Realizar um novo cadastro.'
                               '\n\n-Digite a opção desejada: '))

            if option == 1:
                user.login()

            if option == 2:
                register.novo_cadastro()

        case 2:
            parking.remover_carro()
        case 3:
            parking.vagas()
        case 4:
            option = int(input('Deseja ver que qual relatório?'
                         f'\n1 -{emoji9} Usuários cadastrados'
                               f'\033[32m\n2 -{emoji10} Relatório do dia\033[m'
                               '\n\n-Digite a opção desejada: '))
            if option == 1:
                user.relatorio_clientes()
            if option == 2:
                parking.relatorio_parking()
        case 5:
            parking.liberar()
        case 6:
            break
