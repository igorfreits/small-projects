# Mensagens de erro e suas respectivas chaves do contador
erros = {
    'Fornecedor': 'fornecedor',
    'Accouting aérea não possui trechos': 'sem_trecho',
    'Falta informar o status no trecho': 'sem_trecho',
    'Bilhete deve ter 10 caracteres!': 'bilhete_incompleto',
    'Pnr já existente. A duplicidade de rloc': 'rloc_duplicado',
    'não pree': 'nao_preenchido',
    'VerificaÃ§Ã£o de bilhetes': 'bilhete_duplicado',
    'Não foi possível encontrar um contrato válido para o fornecedor': 'contrato_inspirado',
    'Este cliente não possui permissão para usar este tipo de pagamento': 'cobraca_nao_permitida',
    'Módulo Operações': 'pagamento_indevido',
    'conciliada no BSP': 'bilhete_conciliado',
    'is not a valid integer value': 'caracter_invalido',
    'name contained an invalid character': 'caracter_invalido',
    'valor permitido!': 'nao_preenchido',
    'Necessário cadastrar um contrato para o cliente': 'cliente_sem_contrato',
    'Erro excluindo PNR:': 'alterada_baixa',
    'Erro ao processar PNR ': 'alterada_baixa',
    '.xlsx': 'alterada_baixa',
    'A name was started with an invalid character': 'caracter_invalido',
    'possui uma transação de cartão efetivada': 'pagamento_indevido',
}

# Mensagens de vendas manuais que não devem ser substituídas
lancamento_manual = [
    'Reserva importada via planilh',
    'obs', 'Venda importada pela captura de reserva no Middleware!',
    'SOLICITAÇÃO FEITA PELO EMERGENCIAL', 'Código do emissor SP_I_I',
    '.C criado pela equipe da conciliação aérea para ajuste na forma de pagamento e recebimento',
    'Bagagem', 'CONTABILIZAÇÃO BAGAGEM', 'CONTABILIZAÇÃO BAGAGEM', 'NAO TEM NO GOVER',
    'Reemissão Involuntária', 'Pet', 'LA*MUILLC', 'SOLICITANTE: MARCELO',
    'COMPRA DE BAGAGEM EXTRA', 'HOTEL', 'CONTABILIZAÇÃO DE ALTERAÇÃO', 'ASSENTO GOL MAIS CONFORTO'
]

# chaves do contador e suas informações
list_erros = {
    'fornecedor': 'Falta de Fornecedor',
    'bilhete_incompleto': 'Bilhete incompleto',
    'bilhete_duplicado': 'Bilhete duplicado',
    'rloc_duplicado': 'Duplicidade de RLOC',
    'alterada_baixa': 'Alteração após baixa',
    'contrato_inspirado': 'Contrato de fornecedor Inspirado',
    'pagamento_indevido': 'Forma de Pagamento indevida',
    'sem_trecho': 'Accounting sem trecho',
    'cliente_sem_contrato': 'Cliente sem contrato de fornecedor',
    'nao_preenchido': 'Falta de informação Gerencial',
    'caracter_invalido': 'Caracter inválido',
    'cobraca_nao_permitida': 'Pagamento não permitido para cobrança',
    'bilhete_conciliado': 'Bilhete conciliado'
}

meses_por_extenso = {
    '/01/': 'Janeiro', '/02/': 'Fevereiro', '/03/': 'Março',
    '/04/': 'Abril', '/05/': 'Maio', '/06/': 'Junho',
    '/07/': 'Julho', '/08/': 'Agosto', '/09/': 'Setembro',
    '/10/': 'Outubro', '/11/': 'Novembro', '/12/': 'Dezembro'
}