import win32com.client as win32
import pandas as pd
from datetime import datetime


def envio_email():

    resumo_geral = pd.read_excel(
        r'C:\Users\igorsantos\Desktop\DOCS\PROCESSADO ERRO\AUDITORIA DO PROCESSADO ERRO.xlsx', sheet_name='Resumo Geral')

    resumo_resolvidos = pd.read_excel(
        r'C:\Users\igorsantos\Desktop\DOCS\PROCESSADO ERRO\AUDITORIA DO PROCESSADO ERRO.xlsx', sheet_name='Resumo Resolvidos')

    casos_novos = resumo_geral.iloc[4, 5]
    casos_resolvidos = resumo_geral.iloc[12, 5]

    grupos_empresariais = []
    for x in range(4, 9):
        grupos_empresariais.append(resumo_geral.iloc[x, 14])

    aging = []
    for x in range(6, 8):
        aging.append(resumo_geral.iloc[x, 5])

    rlocs_duplicados = []
    for row in range(32, 100):
        if 'Total Geral' in resumo_resolvidos.iloc[row, 7]:
            break
        rlocs_duplicados.append(resumo_resolvidos.iloc[row, 7])

    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)

    email.to = 'rafaelzizzi@kontik.com.br;camilasilva@kontik.com.br;lanatakuma@kontik.com.br;reinildosantos@kontik.com.br;yurirodrigues@kontik.com.br;brunomoreira@kontik.com.br;angelasilva@zupper.com.br;wagneyoliveira@kontik.com.br;icaroxavier@kontik.com.br;raulneik.parceiro@kontik.com.br;thiagobatello@kontik.com.br'
    email.CC = 'danilocardoso@kontik.com.br;josemonalmeida@kontik.com.br;luisvasquez@kontik.com.br;pliniocarvalhosp@kontik.com.br;alexandrecastro@kontik.com.br;conciliacao_aereo@kontik.com.br'

    email.Subject = f'Análise de Erros - {datetime.now().strftime("%d/%m/%Y")}'

    email.HTMLBody = f"""
    <p>Bom dia a todos,</p>
    <p></p>
    <p>Segue análise do Processado erro com base no arquivo recebido hoje. </p>
    <p></p>
    <strong><h4>ATENÇÃO AO BAIXAR OS ANEXOS!</h4></strong>
    <p></p>
    <p>Pontos analisados:</p>

        <blockquote><p> 1) Casos novos {casos_novos}, saíram {casos_resolvidos};</p></blockquote>
        <blockquote><p> 2) {'[%s]' % ', '.join(map(str, grupos_empresariais))}. São os que mais impactam no relatório;</p></blockquote>
        <blockquote><p> 3) Temos {sum(aging)} casos com Aging acima de 15 dias.</p></blockquote>
        <blockquote><p> 4) Temos {len(rlocs_duplicados)} casos que já haviam sido resolvidos, mas voltaram no relatório: {
        '[%s]' % ', '.join(map(str, rlocs_duplicados))}.</p></blockquote>
        <blockquote><p> 5) Há quantidade de vendas por parte da HubTravel está elevado, pois existem vendas sem a forma de pagamento inserido + Mensagem de Erro</p></blockquote>
    <p></p>
    <p></p>
    """
    relatorio = r'C:\Users\igorsantos\Desktop\DOCS\saves\Relatorio.xlsx'
    relatorio_zk = r'C:\Users\igorsantos\Desktop\DOCS\saves\Relatorio(Zupper e Kontrip).xlsx'
    auditoria_pdf = r'C:\Users\igorsantos\Desktop\DOCS\PROCESSADO ERRO\AUDITORIA DO PROCESSADO ERRO - ' + \
        f'{datetime.now().strftime("%d.%m.%Y")}.pdf'

    email.Attachments.Add(relatorio)
    email.Attachments.Add(relatorio_zk)
    email.Attachments.Add(auditoria_pdf)
    email.Save()

    print('\033[1;32mEmail criado com sucesso!\033[m')


envio_email()
