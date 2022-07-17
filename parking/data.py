from random import randint
import string
from random import choice, randrange
from emoji import emojize,  demojize


lista_de_carros = ['CELTA', 'UNO', 'CAMARO', 'VERONA', 'CORSA', 'GOL', 'PALIO',
                   'FUSCA', 'FIESTA', 'FOX', 'UP', 'GOLF', 'CIVIC', 'CRUZE', 'ONIX', 'PUNTO',
                   'HB20', 'KIA', 'SANDERO', 'RENEGADE', 'COROLLA', 'POLO', 'HILUX', 'S10',
                   'CHIRON', 'VENENO', 'TUATARA', 'IDEA', '250GTO']


emoji1 = emojize(':parking:', use_aliases=True)
emoji2 = emojize(':carro_se_aproximando:', language='pt')
emoji3 = emojize(':gráfico_subindo:', language='pt')
emoji4 = emojize(':proibido:', language='pt')
emoji5 = emojize(':botão_de_xis:', language='pt')
emoji6 = emojize(':mapa-múndi:', language='pt')
emoji7 = emojize(':alien_monster:')
emoji8 = emojize(':rocket:')
emoji9 = emojize(':bookmark_tabs:')
emoji10 = emojize(':money_with_wings:')


def placa_generate():
    a = randrange(100, 999)
    tamanho = 4
    letras = string.ascii_uppercase
    b = ''
    for i in range(tamanho):
        b += choice(letras)
    c = b+'-'+str(a)
    return c


def cpf_generate():
    n1 = str(randint(100000000, 999999999))
    novo_cpf = n1
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
                total = 0
            novo_cpf += str(d)

    return novo_cpf


def id():
    a = randrange(100, 999)
    return a
