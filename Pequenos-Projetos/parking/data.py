import string
from random import choice, randrange
from emoji import emojize


lista_de_carros = ['celta', 'uno', 'camaro', 'verona', 'corsa', 'gol', 'palio',
                   'fusca', 'fiesta', 'fox', 'up']


a = randrange(100, 999)
tamanho = 4
letras = string.ascii_uppercase
b = ''
for i in range(tamanho):
    b += choice(letras)

c = b+'-'+str(a)

emoji1 = emojize(':parking:', use_aliases=True)
emoji2 = emojize(':carro_se_aproximando:', language='pt')
emoji3 = emojize(':gráfico_subindo:', language='pt')
emoji4 = emojize(':proibido:', language='pt')
emoji5 = emojize(':botão_de_xis:', language='pt')
emoji6 = emojize(':mapa-múndi:', language='pt')

print(c)
print(c)