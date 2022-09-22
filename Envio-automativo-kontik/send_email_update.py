import win32com.client as win32


class SendEmail:
    def __init__(self, remetente, destino):
        self.email = remetente
        self.destino = destino

    def send_outlook(self):
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)

        email.To = self.destino
        email.Subject = "UPDATE"

        email.HTMLBody = """
        <p>Olá! <b>Teste</b>, sou um e-mail gerado automaticamente!</b></p>

        <p>O sistema de automação foi concluído com sucesso e por isso,
        não se preocupe.</p>

        <p>Até a próxima...</p>
        """

        email.Attachments.Add(
            r'INSIRA O CAMINHO DO ARQUIVO GERADO')

        email.Attachments.Add(
            r'INSIRA O CAMINHO DO ARQUIVO GERADO')

        try:
            email.Send()
            print('\033[32mE-mail enviado com sucesso!\033[m')
        except Exception as e:
            print('\033[31mErro ao enviar o e-mail, tente novamente!\033[m')
            print(e)
