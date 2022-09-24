from generate_files import ComandosACC, ComandosPNR
from send_email_update import SendEmail


acc = ComandosACC().insert()
pnr = ComandosPNR().insert()


option = input('Deseja enviar o e-mail? [S/N] ').upper()

if option == 'S':

    send_email = SendEmail(remetente='igorsantos@kontik.com.br',
                           destino='josemonalmeida@kontik.com.br')
    send_email.send_outlook()

else:
    print('\033[31mE-mail não enviado!\033[m')
