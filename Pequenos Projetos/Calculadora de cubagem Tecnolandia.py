import requests
from tkinter import *

tpc = 4900  # 100 metros de tpc s/ malha
tpcm = 5800  # 100 metros tpc com malha
trc = 10  # 1 metro de trc
dreno = 57  # 1 metro de dreno
pvc_piso = 25.5  # 1 metro de pvc para piso - verde

carretel = 1550
caixa = 3000  # 50x50x60

cubagem = 0

while cubagem == 0:
    m = int(input('quantidade: '))

    tipo = input('Material:'
                 '\n TPC= 1'
                 '\n TPC com MaLha metálica = 2'
                 '\n TRC = 3'
                 '\n DRENO = 4'
                 '\n PVC para piso = 5'
                 '\n ...')

    if tipo == '1':
        mts = m / 100
        v1 = tpc * mts
        print(f'O peso de {m} mts de TPC s/ malha valem: {v1} gramas')

    elif tipo == '2':
        mts = m / 100
        v1 = tpcm * mts
        print(f'O peso de {m} mts de TPC com malha valem: {v1} gramas')

    elif tipo == '3':
        v1 = trc * m
        v2 = trc * m + carretel
        c = input('ira em carretel? [1] SIM ou [2] NAO'
                  '\n ...')

        if c == '1':
            print(
                f'O peso de {m} mts de TRC em um carretel valem: {v2} gramas')
        else:
            print(
                f'O peso de {m} mts de TRC sem o  carretel valem: {v1} gramas')

    elif tipo == '4':
        q = int(input('Metros das pecas em dreno: '))
        v1 = dreno * q * m
        print(f'O peso de {m} drenos de {q} mts valem: {v1} gramas')

    elif tipo == '5':
        w300 = 15
        w500 = 25
        w700 = 35
        w900 = 45
        a = (input('Insira o watts da peca? "300", "500", "700", "900"'
                   '\n...'))

        if a == '300':
            b = pvc_piso * w300 * m
            print(f'O peso de {m} pecas de pvc com {a} W valem: {b} gramas')

        elif a == '500':
            b = pvc_piso * w500 * m
            print(f'O peso de {m} pecas de pvc com {a} W valem: {b} gramas')

        elif a == '700':
            b = pvc_piso * w700 * m
            print(f'O peso de {m} pecas de pvc com {a} W valem: {b} gramas')

        elif a == '900':
            b = pvc_piso * w900 * m
            print(f'O peso de {m} pecas de pvc com {a} W valem: {b} gramas')
    cubagem += 1

# Inicio janela
janela = Tk()

janela.title('Cubagem Tecnolatina')

texto_orientação = Labe(janela, text='')

janela.mainloop()  
