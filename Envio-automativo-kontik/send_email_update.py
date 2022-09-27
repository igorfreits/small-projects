class SendEmail:
    def __init__(self, remetente, destino, copia):
        self.email = remetente
        self.destino = destino
        self.copia = copia
        self.rename_file()
        self.send_outlook()
        self.delete_file()

    def rename_file(self):
        from os import rename

        self.nome = input('-Digite o nome e/ou tipo do arquivo: ').upper()

        try:
            rename('_ACC.txt', f'{self.nome}_ACC.txt')
            rename('_PNR.txt', f'{self.nome}_PNR.txt')
            print('\033[32m-Arquivos renomeados com sucesso!\033[m')
        except FileNotFoundError:
            print('\033[31m-Arquivos não encontrados!\033[m')

    def send_outlook(self):
        import win32com.client as win32
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)

        email.To = self.destino
        email.Subject = f"UPDATE - {self.nome}"
        email.CC = self.copia

        email.HTMLBody = f"""
        <p>Olá! <b>Usuários</b>, Segue o UPDATE de {self.nome}.</p>
        <p>Até a próxima...</p>
        """

        file_acc = 'INSIRA O LOCAL DO ARQUIVO "_ACC"' + \
            f'\\{self.nome}_ACC.txt'

        file_pnr = 'INSIRA O LOCAL DO ARQUIVO "_PNR"' + \
            f'\\{self.nome}_PNR.txt'

        file_excel = 'INSIRA O LOCAL DO ARQUIVO EXCEL'

        email.Attachments.Add(file_acc)
        email.Attachments.Add(file_pnr)
        email.Attachments.Add(file_excel)

        try:
            email.Send()
            print('\033[32m-E-mail enviado com sucesso!\033[m')
        except Exception as e:
            print('\033[31m-Erro ao enviar o e-mail, tente novamente!\033[m')
            print(e)

    def delete_file(self):
        from os import remove
        from time import sleep

        try:
            print(
                '\033[31m-Deletando arquivos gerados, caso necessite, verifique seu e-mail...\033[m')
            sleep(2)
            remove(f'{self.nome}_ACC.txt')
            remove(f'{self.nome}_PNR.txt')
            print('\033[32m-Arquivos excluídos com sucesso!\033[m')
        except FileNotFoundError:
            print('\033[31m-Arquivos não encontrados!\033[m')
