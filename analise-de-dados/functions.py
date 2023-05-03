from openpyxl.styles import Font, PatternFill, Alignment


def contador_erros():
    erros = {
        'fornecedor': 0, 'sem_trecho': 0, 'rloc_duplicado': 0, 'info_gerencial': 0, 'bilhete_duplicado': 0,
        'bilhete_incompleto': 0, 'contrato_inspirado': 0, 'cobraca_nao_permitida': 0,
        'pagamento_indevido': 0, 'bilhete_conciliado': 0, 'acc_duplicado':0,
        'caracter_invalido': 0, 'alterada_baixa': 0, 'cliente_sem_contrato': 0,
        'tarifa_incorreta': 0, 'conciliacao_cartao': 0, 'reprocessar_venda': 0,
        'nao_indentificado': 0, 'venda_sem_pagamento': 0
    }

    return erros


def custom_guia(guia, a, b, cor, font='FFFFFFFF'):
    for cell in guia[a:b]:
        for c in cell:
            c.fill = PatternFill(start_color=cor,
                                 end_color=cor,
                                 fill_type='solid')
            c.font = Font(color=font, bold=True)
            c.alignment = Alignment(horizontal='center')


def tamanho_coluna(sheet1, sheet2):
    sheet1.column_dimensions['A'].width = 16
    sheet1.column_dimensions['B'].width = 15
    sheet1.column_dimensions['C'].width = 40
    sheet1.column_dimensions['D'].width = 90
    sheet1.column_dimensions['E'].width = 90
    sheet1.column_dimensions['F'].width = 25

    sheet2.column_dimensions['D'].width = 20
    sheet2.column_dimensions['F'].width = 20
    sheet2.column_dimensions['G'].width = 20
    sheet2.column_dimensions['H'].width = 20
    sheet2.column_dimensions['I'].width = 22
    sheet2.column_dimensions['AK'].width = 55
    sheet2.column_dimensions['AL'].width = 90

    return sheet1, sheet2

def nome_colunas(sheet1, sheet2):
    sheet1['A1'] = 'OBTS'
    sheet1['B1'] = 'QUANTIDADE'
    sheet1['C1'] = 'TIPO DE ERRO'
    sheet1['D1'] = 'CAUSA'
    sheet1['E1'] = 'SOLUÇÃO'
    sheet1['F1'] = 'RESPONSÁVEL'


    sheet2['A1'] = 'Handle PNR'
    sheet2['B1'] = 'Handle ACC'
    sheet2['C1'] = 'Sequencia'
    sheet2['D1'] = 'Data Inclusão'
    sheet2['E1'] = 'Data Alteração'
    sheet2['F1'] = 'Número da Semana'
    sheet2['G1'] = 'Mês Alteração'
    sheet2['H1'] = 'Dias Parados no Erro'
    sheet2['I1'] = 'Localizadora'
    sheet2['J1'] = 'Pax'
    sheet2['K1'] = 'Agente'
    sheet2['L1'] = 'Data Emissão'
    sheet2['M1'] = 'Requisição'
    sheet2['N1'] = 'Local Retirada'
    sheet2['O1'] = 'Status Requisicao'
    sheet2['P1'] = 'Forma Pagamento'
    sheet2['Q1'] = 'Forma Recebimento'
    sheet2['R1'] = 'Serviço'
    sheet2['S1'] = 'Cancelado'
    sheet2['T1'] = 'Grupo Empresarial'
    sheet2['U1'] = 'Cliente'
    sheet2['V1'] = 'Cliente Fee POS'
    sheet2['W1'] = 'Fornecedor'
    sheet2['X1'] = 'Hotel Nome'
    sheet2['Y1'] = 'Hotel Codigo'
    sheet2['Z1'] = 'Hotel Broker'
    sheet2['AA1'] = 'Filial'
    sheet2['AB1'] = 'Canal de Vendas'
    sheet2['AC1'] = 'Codigo Evento'
    sheet2['AD1'] = 'Equipe Multifuncional'
    sheet2['AE1'] = 'Tarifa'
    sheet2['AF1'] = 'Taxa'
    sheet2['AG1'] = 'Outras Taxas'
    sheet2['AH1'] = 'Taxa DU'
    sheet2['AI1'] = 'Taxa BR'
    sheet2['AJ1'] = 'Taxa Extra'
    sheet2['AK1'] = 'Observação'
    sheet2['AL1'] = 'Mensagem Erro'
    sheet2['AM1'] = 'OBTS'
    sheet2['AN1'] = 'TIPO DE ERRO'
    sheet2['AO1'] = 'CAUSA'
    sheet2['AP1'] = 'SOLUÇÃO'
    sheet2['AQ1'] = 'RESPONSÁVEL'

    return sheet1, sheet2