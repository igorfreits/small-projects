from generate_files import ComandosACC, ComandosPNR
from send_email_update import SendEmail


if '__main__' == __name__:
    ComandosACC()
    ComandosPNR()

    option = input('-Para enviar o e-mail digite "S"'
                   '\n...').upper()

    if option == 'S':
        try:
            SendEmail(remetente='INSIRA O E-MAIL DO REMETENTE',
                      destino='INSIRA O E-MAIL DO DESTINO')
        except Exception as e:
            print(e)
            print('\033[31m-E-mail não enviado!\033[m')

    else:
        print('\033[31m-E-mail não enviado!\033[m')
