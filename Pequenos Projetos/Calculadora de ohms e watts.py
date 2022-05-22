print('\033[0;34m Bem vindo a Lei de ohms!\033[m')
msg = (input('Qual calculo voce gostaria de fazer? '
             '\n Digite 1 para calcular os\033[0;35m OHMS \033[m'
             '\n Digite 2 para calcular a\033[0;35m  POTENCIA (W) \033[m'
             '\n ...'))

if msg == '1':
    print('\033[0;36m Voce escolheu calcular os ohms! \033[m')
    volts1 = int(input('Digite a voltagem: '))
    comp1 = int((input('Digite o comprimento da peca em \033[0;31m MM \033[m: ')))
    compm = int(comp1 / 1000)
    w1 = float((input('Digite a potencia: ')))
    potencia = int(input('Qual o tipo de watts?'
                         '\n Digite 1 para calcular W/M (\033[0;34mWATTS POR METRO\033[m)'
                         '\n Digite 2 para calcular W/T (\033[0;34mWATTS TOTAL\033[m)'
                         '\n ...'))
    if potencia == 1:
        ohms1 = (volts1 * volts1) / w1 / compm / compm
        print(f'Sua peca tem uma voltagem de \033[0;31m{volts1}V\033[m,'
              f'mede \033[0;34m{compm} metros\033[m, '
              f'uma potencia de \033[0;35m{w1} W/M\033[m'
              f'\n e tem \033[0;33m{ohms1:.2f} ohms\033[m por metro')
    elif potencia == 2:
        ohms = (volts1 * volts1) / w1 / compm
        print(f'Sua peca tem uma voltagem de \033[0;31m{volts1}V\033[m,'
              f'mede \033[0;34m{compm} metros\033[m, '
              f'uma potencia de \033[0;35m{w1} W/T\033[m'
              f'\ne tem \033[0;33m{ohms:.2f} ohms\033[m por metro')
elif msg == '2':
    print('\033[0;33m Voce escolheu calcular os watts! \033[m')
    volts = int(input('Digite a voltagem: '))
    comp2 = int(input('Digite o comprimento da peca \033[0;31m MM \033[m: '))
    compmm = int(comp2 / 1000)
    ohms_metro = int(input('Digite os ohms: '))
    ohms_total = compmm * ohms_metro
    watts_total = (volts * volts) / ohms_total
    watts_metro = (volts * volts) / ohms_total / compmm
    print(f'Sua peca tem uma voltagem de \033[0;31m{volts}V\033[m,'
          f'mede \033[0;34m{compmm} metros\033[m, '
          f'tem uma potencia total de \033[0;35m{watts_total:.2f} W/T \033[m e '
          f' com cerca de \033[0;31m{watts_metro:.2f} W/M \033[m')
else:
    print("\033[0;36m Tecnolatina s2 \033[m")
    