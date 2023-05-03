from openpyxl import Workbook
import pandas as pd
from functions import custom_guia, contador_erros, tamanho_coluna, nome_colunas
from datetime import datetime
from mensagens_erro import meses_por_extenso, lancamento_manual, list_erros
from info import informacoes
from openpyxl.styles import Font


def analise_dados():
    arquivo = pd.read_excel(
        'small-projects/analise-de-dados/data/Processado Erro.xlsx') 
    msg_erros = pd.read_excel(
        'small-projects/analise-de-dados/data/Parametros.xlsx', sheet_name='Parametros')

    arquivo['Observação'].fillna('Venda Manual', inplace=True)
    arquivo.fillna('-', inplace=True)

    for row in range(len(arquivo)):
        if 'ZUPPER' in arquivo['Canal de Vendas'][row] \
            or 'KONTRIP' in arquivo['Canal de Vendas'][row] \
                or 'Zupper' in arquivo['Canal de Vendas'][row]\
                or 'Zupper' in arquivo['Grupo Empresarial'][row]\
                or 'Zupper' in arquivo['Agente'][row]:
            arquivo.drop(row, inplace=True)

    arquivo['Mês Alteração'] = ''
    arquivo['Número da Semana'] = ''
    arquivo['Dias Parados no Erro'] = ''

    arquivo.to_excel(
        'small-projects/analise-de-dados/data/Processado Erro.xlsx', index=False)

    for manual in lancamento_manual:
        for x in range(len(arquivo)):
            if manual in arquivo['Observação'][x]:
                arquivo['Observação'][x] = 'Venda Manual'

    obts = ['Gover', 'TMS', 'HubTravel', 'Lemontech', 'Venda Manual']

    contador = {
        'Gover':
        contador_erros(),
        'TMS':
        contador_erros(),
        'HubTravel':
        contador_erros(),
        'Lemontech':
        contador_erros(),
        'Venda Manual':
        contador_erros()
    }

    for x in range(len(arquivo)):
        if '?' in arquivo['Forma Pagamento'][x]:
            arquivo['Mensagem Erro'][x] = 'Inserir forma de pagamento'

        if 'N/I' in arquivo['Pax'][x] and 'Gover' in arquivo['Observação']:
            arquivo['Mensagem Erro'][x] = 'Accounting Duplicado'

    for linha in range(len(arquivo)):
        arquivo['Dias Parados no Erro'][linha] = (
            datetime.now() - datetime.strptime(arquivo['Data Inclusão'][linha], '%d/%m/%Y %H:%M:%S')).days
                      
    file_relatorio = Workbook()
    sheet1 = file_relatorio.active

    sheet1.title = 'Analise'
    sheet2 = file_relatorio.create_sheet('Processado Erro')

    tamanho_coluna(sheet1, sheet2)

    nome_colunas(sheet1, sheet2)



    for x in range(len(arquivo)):
        sheet2.append([arquivo['Handle PNR'][x], arquivo['Handle ACC'][x],
                       arquivo['Sequencia'][x], arquivo['Data Inclusão'][x],
                       arquivo['Data Alteração'][x], arquivo['Número da Semana'][x],
                       arquivo['Mês Alteração'][x], arquivo['Dias Parados no Erro'][x],
                       arquivo['Localizadora'][x], arquivo['Pax'][x], arquivo['Agente'][x],
                       arquivo['Data Emissão'][x], arquivo['Requisição'][x],
                       arquivo['Local Retirada'][x], arquivo['Status Requisicao'][x],
                       arquivo['Forma Pagamento'][x], arquivo['Forma Recebimento'][x],
                       arquivo['Serviço'][x], arquivo['Cancelado'][x],
                       arquivo['Grupo Empresarial'][x], arquivo['Cliente'][x],
                       arquivo['Cliente Fee POS'][x], arquivo['Fornecedor'][x],
                       arquivo['Hotel Nome'][x], arquivo['Hotel Codigo'][x],
                       arquivo['Hotel Broker'][x], arquivo['Filial'][x],
                       arquivo['Canal de Vendas'][x], arquivo['Codigo Evento'][x],
                       arquivo['Equipe Multifuncional'][x], arquivo['Tarifa'][x],
                       arquivo['Taxa'][x], arquivo['Outras Taxas'][x], arquivo['Taxa DU'][x],
                       arquivo['Taxa BR'][x], arquivo['Taxa Extra'][x],
                       arquivo['Observação'][x], arquivo['Mensagem Erro'][x]
                       ])

    sheet1['A1'] = 'OBTS'
    sheet1['B1'] = 'QUANTIDADE'
    sheet1['C1'] = 'TIPO DE ERRO'
    sheet1['D1'] = 'CAUSA'
    sheet1['E1'] = 'SOLUÇÃO'
    sheet1['F1'] = 'RESPONSÁVEL'

    for linha in range(len(arquivo)):
        for days in meses_por_extenso:
            if days in sheet2['D' + str(linha + 2)].value:
                if '2018' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2018'
                elif '2019' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2019'
                elif '2020' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2020'
                elif '2021' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2021'
                elif '2022' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2022'
                elif '2023' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)] = f'{meses_por_extenso[days]} de 2023'

    for linha in range(len(arquivo)):
        sheet2['F' + str(linha + 2)] = f'=NÚMSEMANA(D{linha + 2})'

    custom_guia(sheet1, 'A1', 'F1', '000080FF')
    custom_guia(sheet2, 'A1', 'AQ1', '000080FF')

    for linha in range(len(arquivo)):
        if sheet2['H' + str(linha + 2)].value > 15:
            sheet2['H' + str(linha + 2)].font = Font(color='FF0000')


    for row in range(len(arquivo)):
        for row2 in range(len(msg_erros)):
            if msg_erros['Mensagem'][row2] in arquivo['Mensagem Erro'][row]:
                sheet2['AN' + str(row + 2)] = msg_erros['Campo'][row2]

    for row in range(len(arquivo)):
        for obt in contador:
            if obt in arquivo['Observação'][row]:
                sheet2['AM' + str(row + 2)] = obt
            if 'TMS' in arquivo['Observação'][row]:
                sheet2['AM' + str(row + 2)] = 'Argo'

    for row in range(len(arquivo)):
        if sheet2['AN' + str(row + 2)].value is None:
            sheet2['AN' + str(row + 2)] = 'Não identificado'
            sheet2['AO' + str(row + 2)] = 'Reportar ao responsável'
            sheet2['AP' + str(row + 2)] = 'Reportar ao responsável'
            sheet2['AQ' + str(row + 2)] = 'Reportar ao responsável'

    for row in range(len(arquivo)):
        for x, y in list_erros.items():
            if y in sheet2['AN' + str(row + 2)].value:
                sheet2['AO' + str(row + 2)] = informacoes[y]['causa']
                sheet2['AP' + str(row + 2)] = informacoes[y]['solucao']
                sheet2['AQ' + str(row + 2)] = informacoes[y]['responsavel']

    for obt in obts:
        for tipo, msg in list_erros.items():
            for row in range(len(arquivo)):
            
                if obt in arquivo['Observação'][row]:
                    if msg in sheet2['AN' + str(row + 2)].value:
                        contador[obt][tipo] += 1

    for obt in contador:
        for x, y in list_erros.items():
            if contador[obt][x] > 0:
                sheet1.append([obt, contador[obt][x], y,
                               informacoes[y]['causa'], informacoes[y]['solucao'], informacoes[y]['responsavel']])
                

    for row in range(len(sheet1['A'])):
        if 'TMS' in sheet1['A' + str(row + 1)].value:
            sheet1['A' + str(row + 1)] = 'Argo'


    cont_localizador = []

    for row in range(len(arquivo)):
        cont_localizador.append(sheet2['I' + str(row + 2)].value)

        if cont_localizador.count(sheet2['I' + str(row + 2)].value) > 15:
            sheet2['AN' + str(row + 2)] = 'Gover/Bosch envia venda cancelada'
            sheet2['AO' + str(row + 2)] = 'Envio de venda cancelada'
            sheet2['AP' + str(row + 2)] = 'Remoção da integração e exclusão do portal'
            sheet2['AQ' + str(row + 2)] = 'Dnit e Suporte Benner'

    file_relatorio.save('small-projects/analise-de-dados/Relatorio.xlsx')
    print('-Processando...')


try:
    analise_dados()

except KeyError:
    analise_dados()
finally:
    analise_dados()

print('\033[1;32m-Relatório gerado com sucesso!\033[m')
