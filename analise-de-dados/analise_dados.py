from openpyxl import Workbook
import pandas as pd
from mensagens_erro import erros, lancamento_manual, list_erros, meses_por_extenso
from infos import infomacoes
from functions import contador_erros, custom_guia

arquivo = pd.read_excel(
    'data/Processado Erro.xlsx')

arquivo['Observação'].fillna('Venda Manual', inplace=True)
arquivo.fillna('-', inplace=True)

for row in range(len(arquivo)):
    if 'ZUPPER' in arquivo['Canal de Vendas'][row] \
            or 'KONTRIP' in arquivo['Canal de Vendas'][row]:
        arquivo.drop(row, inplace=True)


arquivo['Número da Semana'] = ''
arquivo['Mês de Alteração'] = ''


for linha in range(len(arquivo)):
    for days in meses_por_extenso:

        if days in arquivo['Data Alteração'][linha]:
            if '/2022' in arquivo['Data Alteração'][linha]:
                arquivo['Data Alteração'][linha] = f'{meses_por_extenso[days]} de 2022'

            if '/2023' in arquivo['Data Alteração'][linha]:
                arquivo['Data Alteração'][linha] = f'{meses_por_extenso[days]} de 2023'

arquivo.to_excel('data/Processado Erro.xlsx', index=False)


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
        contador_erros(),
}


for manual in lancamento_manual:
    for x in range(len(arquivo)):
        if manual in arquivo['Observação'][x]:
            arquivo['Observação'][x] = 'Venda Manual'

obts = ['Gover', 'TMS', 'HubTravel',
        'Lemontech', 'Venda Manual']

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
sheet2.column_dimensions['J'].width = 22
sheet2.column_dimensions['AH'].width = 102
sheet2.column_dimensions['AI'].width = 145

sheet2['A1'] = 'Handle PNR'
sheet2['B1'] = 'Handle ACC'
sheet2['C1'] = 'Sequencia'
sheet2['D1'] = 'Data Inclusão'
sheet2['E1'] = 'Data Alteração'
sheet2['F1'] = 'Número da Semana'
sheet2['G1'] = 'Mês de Alteração'
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

for x in range(len(arquivo)):
    sheet2.append([arquivo['Handle PNR'][x], arquivo['Handle ACC'][x],
                   arquivo['Sequencia'][x], arquivo['Data Inclusão'][x],
                   arquivo['Data Alteração'][x], arquivo['Número da Semana'][x],
                   arquivo['Mês de Alteração'][x], arquivo['Localizadora'][x],
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


custom_guia(sheet1, 'A1', 'F1')
custom_guia(sheet2, 'A1', 'AI1')

contador['Argo'] = contador.pop('TMS')
contador = dict(sorted(contador.items()))


for obt in contador:
    for x, y in list_erros.items():
        if contador[obt][x] > 0:
            sheet1.append([obt, contador[obt][x], y,
                           infomacoes[y]['causa'], infomacoes[y]['solucao'], infomacoes[y]['responsavel']])


file_relatorio.save('Relatorio.xlsx')
print('\033[1;32m-Relatório gerado com sucesso!\033[m')
