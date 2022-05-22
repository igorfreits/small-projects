idade = int('23')
print(idade+3)
idade = idade + 6
print(idade)
print(idade)


def mais_um_ano(idade):
    print('ta dentro dessa funcap')
    return idade + 1


mais_um_ano(43)
filme1 = 'toy story 17'
filme2 = 'A Xuxa contra o baixo Astral'
filme3 = 'matrix 1'

filmes = ['toy story 14', 'xuxa', 'matrix 1']
print(filmes)


def imprime_filmes(filmes_que_quero_imprimir):
    print('A lista de filmes que eu tenho disponivel')
    print(filmes_que_quero_imprimir)


print(filmes[-2])
for filme in filmes:
    print(filmes)
    print('...')


def imprime_filmes(filmes_que_quero_imprimir):
    print('A lista de filmes que eu tenho disponivel')
    for filme in filmes_que_quero_imprimir:
        print(filme)


imprime_filmes(filmes)
