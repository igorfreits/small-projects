# informações para o ralatorio
informacoes = {
    'Falta de informação Gerencial': {
        'causa': 'Não digitado e/ou falta de campo no Gover',
        'solucao': 'Ajustar venda no Gover e/ou em paralelo preencher o campo',
        'responsavel': 'DNIT e Operações'
    },
    'Falta de Fornecedor': {
        'causa': 'Falta de Handle de fornecedores',
        'solucao': 'Novos fornecedores',
        'responsavel': 'TI'
    },
    'Bilhete incompleto': {
        'causa': 'Companias aereas com tamanho de bilhete diferente do padrão e/ou não possuem bilhete',
        'solucao': 'Gerar bilhete via Benner',
        'responsavel': 'TI'
    },
    'Bilhete duplicado': {
        'causa': 'Gover mandou bilhete duplicado e/ou venda alterada após contabilização',
        'solucao': 'Realizar analise dos bilhetes no sistema Benner',
        'responsavel': 'TI'
    },
    'Duplicidade de RLOC': {
        'causa': 'Venda integrada manualmente após OBT ter integrado',
        'solucao': 'Exclusão de RLOC não contabilizado',
        'responsavel': 'Operações'
    },
    'Alteração após baixa': {
        'causa': 'Realizado alteração na venda após contabilização',
        'solucao': 'Operações devem enviar para  faturamento para retirar as baixas e assim ajustar as vendas',
        'responsavel': 'Operações e Faturamento'
    },
    'Contrato de fornecedor Inspirado': {
        'causa': 'Fornecedor com CNPJ Baixado na receita',
        'solucao': 'Enviar  CNPJs ativos de fornecedores para alteração',
        'responsavel': 'TI'
    },
    'Forma de Pagamento indevida': {
        'causa': 'Benner efetua o bloqueio',
        'solucao': 'Inserir forma de pagamento',
        'responsavel': 'Operações'
    },
    'Accounting sem trecho': {
        'causa': 'Instabilidade na integração',
        'solucao': 'Excluir venda e reprocessar',
        'responsavel': 'Operações'
    },
    'Cliente sem contrato de fornecedor': {
        'causa': 'Não encontrado contrato para fornecedor e/ou contrato inspirado',
        'solucao': 'Enviar CNPJs ativos de clientes para alteração',
        'responsavel': 'TI'
    },
    'Pagamento não permitido para cobrança': {
        'causa': 'Venda inserida automaticamente no processado erro',
        'solucao': 'Fazer cobrança de FEE',
        'responsavel': 'Josemon'
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
    }
}

