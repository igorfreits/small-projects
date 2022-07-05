import emoji

a = emoji.emojize(':parking:', use_aliases=True)
b = emoji.emojize(':carro_se_aproximando:', language='pt')
c = emoji.emojize(':gráfico_subindo:', language='pt')
d = emoji.emojize(':proibido:', language='pt')
e = emoji.emojize(':botão_de_xis:', language='pt')
f = emoji.emojize(':mapa-múndi:', language='pt')


while True:
    option = int(input(f'\033[34m{"BEM VINDO AO PARKING ISTOP":-^40}'"\n"
                       f'{"Menu inicial":-^40}\033[m'

                       f'\n1 -{b}  Adicionar veiculo'
                       f'\033[31m \n2 -{f}   Remover veiculo \033[m'
                       f'\033[34m \n3 -{a}   Vagas \033[m'
                       f'\n3 -{c}  Relatório'
                       f'\n4 -{d}  Liberar todos as vagas'
                       f'\033[32m \n4 -{e}  Sair \033[m'

                       f'\n\nDigite a opção desejada: '))
