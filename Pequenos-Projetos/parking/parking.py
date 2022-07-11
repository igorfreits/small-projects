from data import emoji1, emoji2, emoji3, emoji4, emoji5, emoji6
from functions import teste


while True:
    option = int(input(f'\033[34m{"BEM VINDO AO PARKING ISTOP":-^40}'"\n"
                       f'{"Menu inicial":-^40}\033[m'

                       f'\n1 -{emoji2}  Adicionar veiculo'
                       f'\033[31m \n2 -{emoji6}   Remover veiculo \033[m'
                       f'\033[34m \n3 -{emoji1}   Vagas \033[m'
                       f'\n4 -{emoji3}  Relatório'
                       f'\n5 -{emoji4}  Liberar todos as vagas'
                       f'\033[32m \n6 -{emoji5}  Sair \033[m'

                       f'\n\nDigite a opção desejada: '))
    match option:
        case 1:
            car = str(input('Digite o nome do carro: ')).upper().strip()
            teste.adicionar_carro(car)
        case 2:
            teste.remover_carro()

        case 3:
            teste.vagas()
        case 4:
            teste.relatorio()
        case 5:
            teste.liberar()
        case 6:
            break
