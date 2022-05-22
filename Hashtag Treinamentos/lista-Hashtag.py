"""
LISTAS = []
"""

lista_compras = ['banana', 'laranja', 'manga']  # [0,1,2]


print(lista_compras)

print(lista_compras[1])

print(lista_compras[-1])  # mostra ultimo valor e assim sucessivamente


lista_compras.append('Beterraba')  # Adiciona um item ao final da lista

print(lista_compras)


# (posicao na lista, objeto) - Adiciona um objeto na posicao escolhida
lista_compras.insert(1, 'Biscoito')

print(lista_compras)


del lista_compras[4]  # apaga um item na posição escolhida

print(lista_compras)


lista_compras.remove('Biscoito')  # Apaga um item com o nome escolhido

print(lista_compras)


lista_compras.append('carro')

print(lista_compras)


lista_sonhos = []

# Pega informação de uma lista e joga na variável
sonho = lista_compras.pop(-1)

# .pop() apaga o ultimo  objeto da lista

print(sonho)


lista_sonhos.append(sonho)  # adiciona o item da variável na lista

print(lista_sonhos)


# tarelas


tarefas = []

tarefa = input('Insira uma tarefa: ')

tarefas.append(tarefa)
print(tarefas)


while tarefa != '':

    tarefa = input('Insira uma tarefa: ')

    tarefas.append(tarefa)
print(tarefas)


print(tarefas[0:3])  # Escolhe posição de inicio e final que ira mostrar

print(tarefas[:2])  # Do inicio ate a posição 2

print(tarefas[2:])  # da posição 2 ate o final


lojas = ['rio de janeiro', 'sao paulo', 'curitiba']

faturamento = [10000, 20000, 50000]


print(lojas)
print(faturamento)


faturamento.sort()  # Organiza os itens em ordem alfabética ou do maior para o menor
print(faturamento)


faturamento.sort(reverse=True)  # Organiza em ordem decrescente
print(faturamento)


resultados = []

for i in range(3):  # Roda o laço 3 vezes
    tuple = (lojas[i-1], faturamento[i-1])

    resultados.append(tuple)
print(resultados)

print(resultados[1][1])
