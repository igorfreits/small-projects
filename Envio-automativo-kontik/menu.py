from generate_files import ComandosACC, ComandosPNR
from send_email_update import SendEmail


ComandosACC().insert()
ComandosPNR().insert()

SendEmail(remetente='INSIRA SEU E-MAIL',
          destino='INSIRA O DESTINO').send_outlook()
