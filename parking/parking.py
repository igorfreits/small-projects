from data import emoji1, emoji2, emoji3, emoji4, emoji5, emoji6
from functions import a
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

                       f'\n\nDigite a opção desejada: '))
    match option:
        case 1:
            option = int(input('Escolha uma opção: \n'
                         '\n[ 1 ] Inserir dados'
                               '\n[ 2 ] Em breve...'
                               '\n... '))
            if option == 1:
                nome = str(input('Digite seu nome: '))
                car = str(input('Digite o nome do carro: '))

                a.adicionar_carro(nome, car)

            if option == 2:
                pass
                # register.novo_cadastro()

        case 2:
            a.remover_carro()
        case 3:
            a.vagas()
        case 4:
            option = int('Deseja ver que qual relatório?'
                         '\n[ 1 ] Usuários cadastrados(Haverá melhoria no sistema)'
                         '\n[ 2 ] Relatório do dia')
            if option == 1:
                pass
                # user.relatorio_clientes()
            if option == 2:
                a.relatorio_parking()
        case 5:
            a.liberar()
        case 6:
            break
