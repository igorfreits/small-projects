# informações para o ralatorio
informacoes = {
    'Falta de informação Gerencial': {
        'causa': 'Não digitado e/ou falta de campo no Gover',
        'solucao': 'Ajustar venda no Gover e/ou em paralelo preencher o campo',
        'responsavel': 'Operações'
    },
    'Falta de Fornecedor': {
        'causa': 'Falta de Handle de fornecedores',
        'solucao': 'Novos fornecedores',
        'responsavel': 'Suporte Benner e Cadastro'
    },
    'Bilhete incompleto': {
        'causa': 'Companias aereas com tamanho de bilhete diferente do padrão e/ou não possuem bilhete',
        'solucao': 'Gerar bilhete via Benner',
        'responsavel': 'Suporte Benner'
    },
    'Bilhete duplicado': {
        'causa': 'Gover mandou bilhete duplicado e/ou venda alterada após contabilização',
        'solucao': 'Realizar analise dos bilhetes no sistema Benner',
        'responsavel': 'Suporte Benner'
    },
    'Duplicidade de RLOC': {
        'causa': 'Venda integrada manualmente após OBT ter integrado',
        'solucao': 'Exclusão de RLOC não contabilizado',
        'responsavel': 'Suporte Benner'
    },
    'Alteração após baixa': {
        'causa': 'Realizado alteração na venda após contabilização',
        'solucao': 'Operações devem enviar para  faturamento para retirar as baixas e assim ajustar as vendas',
        'responsavel': 'Operações e Faturamento'
    },
    'Contrato de fornecedor Inspirado': {
        'causa': 'Fornecedor com CNPJ Baixado na receita',
        'solucao': 'Enviar  CNPJs ativos de fornecedores para alteração',
        'responsavel': 'Suporte Benner'
    },
    'Forma de Pagamento indevida': {
        'causa': 'Benner efetua o bloqueio',
        'solucao': 'Inserir forma de pagamento',
        'responsavel': 'Operações'
    },
    'Accounting sem trecho': {
        'causa': 'Instabilidade na integração',
        'solucao': 'Excluir venda e reprocessar nova venda',
        'responsavel': 'Operações'
    },
    'Cliente sem contrato de fornecedor': {
        'causa': 'Não encontrado contrato para fornecedor e/ou contrato inspirado',
        'solucao': 'Enviar CNPJs ativos de clientes para alteração',
        'responsavel': 'Suporte Benner'
    },
    'Pagamento não permitido para cobrança': {
        'causa': 'Venda inserida automaticamente no processado erro para alteração de pagamento',
        'solucao': 'Fazer cobrança de FEE',
        'responsavel': 'Suporte Benner (Josemon)'
    },
    'Caractere inválido': {
        'causa': 'Inserido Caractere invalido na venda',
        'solucao': 'Correção e/ou exclusão de caractere do campo',
        'responsavel': 'Operações'
    },
    'Bilhete conciliado': {
        'causa': 'Venda alterada após conciliação do bilhete',
        'solucao': 'Verificar se é possível desconciliar e depois seguir com os ajustes',
        'responsavel': 'Conciliação'
    },
    'Valores da Tarifa': {
        'causa': 'Tarifa excede valor ou é menor que a tarifa do accounting',
        'solucao': 'Ajustar tarifa',
        'responsavel': 'Suporte Benner'
    },
    'Conciliação de Cartão': {
        'causa': 'Tentativa de exclusão de venda com conciliação de cartão',
        'solucao': 'Em caso de venda com conciliação de cartão, não é possível excluir a venda. É necessário desconciliar a venda e depois editar',
        'responsavel': 'Conciliação'
    },
    'Accounting duplicado': {
        'causa': 'Erro de integração no Gover faz com que seja duplicado o Accounting',
        'solucao': 'Excluir Accounting duplicado e reprocessar venda',
        'responsavel': 'Suporte Benner'
    },
    'Reprocessar Venda': {
        'causa': 'Venda aguardando reprocessamento',
        'solucao': 'Reprocessar venda',
        'responsavel': 'Suporte Benner'
    },
    'Venda sem a forma de pagamento/recebimento': {
        'causa': 'Envio de venda sem a forma de pagamento/recebimento',
        'solucao': 'Inserção da forma de pagamento/recebimento',
        'responsavel': 'A Definir'
    },
    'Não identificado': {
        'causa': 'Reportar ao responsável',
        'solucao': 'Reportar ao responsável',
        'responsavel': 'Suporte Benner'
    },
}
