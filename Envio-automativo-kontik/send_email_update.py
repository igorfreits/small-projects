class SendEmail:
    def __init__(self, remetente, destino):
        self.email = remetente
        self.destino = destino

    def send_outlook(self):
        import win32com.client as win32
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)

        email.To = self.destino
        email.Subject = "UPDATE"

        email.HTMLBody = """
        <p>Olá! <b>Josemon</b>, sou um e-mail automático enviado pelo Igor!</b></p>

        <p>O sistema de automação foi concluído com sucesso e por isso, não se preocupe.</p>

        <p>Até a próxima...</p>
        """

        email.Attachments.Add(
            r'C:\Users\igorsantos\OneDrive - Kontik Franstur Viagens e Turismo Ltda\Área de Trabalho\Docs\HOTEL_ACC.txt')
        email.Attachments.Add(
            r'C:\Users\igorsantos\OneDrive - Kontik Franstur Viagens e Turismo Ltda\Área de Trabalho\Docs\HOTEL_PNR.txt')

        try:
            email.Send()
            print('\033[32mE-mail enviado com sucesso!\033[m')
        except Exception as e:
            print('\033[31mErro ao enviar o e-mail, tente novamente!\033[m')
            print(e)
