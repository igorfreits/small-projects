from random import randint
import string
from random import choice, randrange
from emoji import emojize


car_list = ['CELTA', 'UNO', 'CAMARO', 'VERONA', 'CORSA', 'GOL', 'PALIO',
            'FUSCA', 'FIESTA', 'FOX', 'UP', 'GOLF', 'CIVIC', 'CRUZE', 'ONIX', 'PUNTO',
            'HB20', 'KIA', 'SANDERO', 'RENEGADE', 'COROLLA', 'POLO', 'HILUX', 'S10',
            'CHIRON', 'VENENO', 'TUATARA', 'IDEA', '250GTO']


emoji1 = emojize(':parking:', use_aliases=True)
emoji2 = emojize(':carro_se_aproximando:', language='pt')
emoji3 = emojize(':gráfico_subindo:', language='pt')
emoji5 = emojize(':botão_de_xis:', language='pt')
emoji6 = emojize(':mapa-múndi:', language='pt')
emoji7 = emojize(':alien_monster:')
emoji8 = emojize(':rocket:')
emoji9 = emojize(':bookmark_tabs:')
emoji10 = emojize(':money_with_wings:')


def board_generate():
    a = randrange(100, 999)
    size = 4
    letters = string.ascii_uppercase
    b = ''
    for i in range(size):
        b += choice(letters)
    c = b+'-'+str(a)
    return c


def cpf_generate():
    n1 = str(randint(100000000, 999999999))
    new_cpf = n1
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
                total = 0
            new_cpf += str(d)

    return new_cpf


def id():
    a = randrange(100, 999)
    return a
