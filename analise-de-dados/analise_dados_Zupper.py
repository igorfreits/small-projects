from openpyxl import Workbook
import pandas as pd
from functions import custom_guia, contador_erros
from mensagens_erro import meses_por_extenso, erros, erros_msg, list_erros
from info import informacoes


def analise_dados_zupper():
    arquivo = pd.read_excel(
        'data/Processado Erro.xlsx')

    arquivo['Observação'].fillna('Venda Manual', inplace=True)
    arquivo['Mensagem Erro'].fillna(
        'Erro ao processar PNR | A semi colon character was expected', inplace=True)
    arquivo.fillna('-', inplace=True)

    for row in range(len(arquivo)):
        if 'ZUPPER' in arquivo['Canal de Vendas'][row]:
            arquivo['Observação'][row] = 'Venda - Zupper'
        if 'KONTRIP' in arquivo['Canal de Vendas'][row]:
            arquivo['Observação'][row] = 'Venda - Kontrip'

    arquivo['Mês Alteração'] = ''
    arquivo['Número da Semana'] = ''

    arquivo.to_excel('data/Processado Erro.xlsx', index=False)

    for x in range(len(arquivo)):
        if 'Zupper' not in arquivo['Observação'][x] and 'Kontrip' not in arquivo['Observação'][x]:
            arquivo.drop(x, inplace=True)

    arquivo.to_excel('data/Processado Erro.xlsx', index=False)

    obts = ['Kontrip', 'Zupper']

    contador = {
        'Zupper':
        contador_erros(),
        'Kontrip':
        contador_erros()
    }

    for obt in obts:
        for x in range(len(arquivo)):

            if obt in arquivo['Observação'][x]:
                for msg, tipo in erros.items():
                    if msg in arquivo['Mensagem Erro'][x]:
                        contador[obt][tipo] += 1

                if '?' in arquivo['Forma Pagamento'][x]:
                    contador[obt]['pagamento_indevido'] += 1

    for obt in obts:
        if contador[obt]['nao_preenchido'] > 0:
            contador[obt]['nao_preenchido'] = contador[obt]['nao_preenchido'] - \
                contador[obt]['fornecedor']
        else:
            contador[obt]['nao_preenchido'] = contador[obt]['fornecedor'] - \
                contador[obt]['nao_preenchido']

    file_relatorio = Workbook()
    sheet1 = file_relatorio.active

    sheet1.title = 'Analise'
    sheet2 = file_relatorio.create_sheet('Processado Erro')

    sheet1.column_dimensions['A'].width = 16
    sheet1.column_dimensions['B'].width = 15
    sheet1.column_dimensions['C'].width = 40
    sheet1.column_dimensions['D'].width = 90
    sheet1.column_dimensions['E'].width = 90
    sheet1.column_dimensions['F'].width = 25

    sheet2.column_dimensions['E'].width = 20
    sheet2.column_dimensions['F'].width = 20
    sheet2.column_dimensions['G'].width = 20
    sheet2.column_dimensions['J'].width = 22
    sheet2.column_dimensions['AJ'].width = 55
    sheet2.column_dimensions['AK'].width = 100

    sheet2['A1'] = 'Handle PNR'
    sheet2['B1'] = 'Handle ACC'
    sheet2['C1'] = 'Sequencia'
    sheet2['D1'] = 'Data Inclusão'
    sheet2['E1'] = 'Data Alteração'
    sheet2['F1'] = 'Número da Semana'
    sheet2['G1'] = 'Mês Alteração'
    sheet2['H1'] = 'Localizadora'
    sheet2['I1'] = 'Pax'
    sheet2['J1'] = 'Agente'
    sheet2['K1'] = 'Data Emissão'
    sheet2['L1'] = 'Requisição'
    sheet2['M1'] = 'Local Retirada'
    sheet2['N1'] = 'Status Requisicao'
    sheet2['O1'] = 'Forma Pagamento'
    sheet2['P1'] = 'Forma Recebimento'
    sheet2['Q1'] = 'Serviço'
    sheet2['R1'] = 'Cancelado'
    sheet2['S1'] = 'Grupo Empresarial'
    sheet2['T1'] = 'Cliente'
    sheet2['U1'] = 'Cliente Fee POS'
    sheet2['V1'] = 'Fornecedor'
    sheet2['W1'] = 'Hotel Nome'
    sheet2['X1'] = 'Hotel Codigo'
    sheet2['Y1'] = 'Hotel Broker'
    sheet2['Z1'] = 'Filial'
    sheet2['AA1'] = 'Canal de Vendas'
    sheet2['AB1'] = 'Codigo Evento'
    sheet2['AC1'] = 'Equipe Multifuncional'
    sheet2['AD1'] = 'Tarifa'
    sheet2['AE1'] = 'Taxa'
    sheet2['AF1'] = 'Outras Taxas'
    sheet2['AG1'] = 'Taxa DU'
    sheet2['AH1'] = 'Taxa BR'
    sheet2['AI1'] = 'Taxa Extra'
    sheet2['AJ1'] = 'Observação'
    sheet2['AK1'] = 'Mensagem Erro'

    sheet2['AL1'] = 'OBTS'
    sheet2['AM1'] = 'TIPO DE ERRO'
    sheet2['AN1'] = 'CAUSA'
    sheet2['AO1'] = 'SOLUÇÃO'
    sheet2['AP1'] = 'RESPONSÁVEL'

    for x in range(len(arquivo)):
        sheet2.append([arquivo['Handle PNR'][x], arquivo['Handle ACC'][x],
                       arquivo['Sequencia'][x], arquivo['Data Inclusão'][x],
                       arquivo['Data Alteração'][x], arquivo['Número da Semana'][x],
                       arquivo['Mês Alteração'][x], arquivo['Localizadora'][x],
                       arquivo['Pax'][x], arquivo['Agente'][x],
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
                if '/2022' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)
                           ] = f'{meses_por_extenso[days]} de 2022'

                if '/2023' in sheet2['D' + str(linha + 2)].value:
                    sheet2['G' + str(linha + 2)
                           ] = f'{meses_por_extenso[days]} de 2023'

    for linha in range(len(arquivo)):
        sheet2['F' + str(linha + 2)] = f'=NÚMSEMANA(D{linha + 2})'

    custom_guia(sheet1, 'A1', 'F1', '993399')
    custom_guia(sheet2, 'A1', 'AP1', '993399')

    for obt in contador:
        for x, y in list_erros.items():
            if contador[obt][x] > 0:
                sheet1.append([obt, contador[obt][x], y,
                               informacoes[y]['causa'], informacoes[y]['solucao'], informacoes[y]['responsavel']])

    for row in range(len(arquivo)):
        for obt in contador:
            if obt in arquivo['Observação'][row]:
                sheet2['AL' + str(row + 2)] = obt
            if 'TMS' in arquivo['Observação'][row]:
                sheet2['AL' + str(row + 2)] = 'Argo'

    for row in range(len(arquivo)):
        for error, msg in erros_msg.items():
            if error in arquivo['Mensagem Erro'][row]:
                sheet2['AM' + str(row + 2)] = msg

    for row in range(len(arquivo)):
        if sheet2['AM' + str(row + 2)].value is None:
            sheet2['AM' + str(row + 2)] = 'Não identificado'
            sheet2['AN' + str(row + 2)] = 'Reportar ao responsável'
            sheet2['AO' + str(row + 2)] = 'Reportar ao responsável'
            sheet2['AP' + str(row + 2)] = 'Reportar ao responsável'

    for row in range(len(arquivo)):
        for x, y in list_erros.items():
            if y in sheet2['AM' + str(row + 2)].value:
                sheet2['AN' + str(row + 2)] = informacoes[y]['causa']
                sheet2['AO' + str(row + 2)] = informacoes[y]['solucao']
                sheet2['AP' + str(row + 2)] = informacoes[y]['responsavel']

    file_relatorio.save('saves/Relatorio(Zupper e Kontrip).xlsx')
    print('Processando...')


try:
    analise_dados_zupper()

except KeyError:
    analise_dados_zupper()
finally:
    analise_dados_zupper()

print('\033[1;32m-Relatório gerado com sucesso!\033[m')
