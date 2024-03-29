# Comando para retornar o handle do contrato
select pessoa, handle
from bb_forncedorcontratos
where tipo = 2
and pessoa in ("CODIGOS DO HOTEL")

# Comando para inserir o hotel no handle
UPDATE VM_PNRACCOUNTINGS SET FORNECEDOR="CODIGO_PROCV" WHERE HANDLE IN ("HANDLES ACC")

# Comando para atualizar o hotel no handle
UPDATE VM_PNRS SET SITUACAO=1, CONCLUIDO='S',
EXPORTADO='N', AGUARDANDOEMISSAO='N' WHERE HANDLE IN("HANDLE_PNR")

#Comando de busca
# Comando para retornar o nome do hotel e código
select * from gn_pessoas cli
left join bb_forncedorcontratos frn on(frn.pessoa = cli.handle)
where frn.tipo = 2 and cli.handle in (CODIGO HOTEL)

# Comando para buscar hotel pelo endereço
select * from gn_pessoas cli
left join bb_forncedorcontratos frn on(frn.pessoa = cli.handle)
where frn.tipo = 2 and cli.logradouro like '%ENDEREÇO%'

# Comando para buscar hotel pelo nome
select * from gn_pessoas cli
left join bb_forncedorcontratos frn on(frn.pessoa = cli.handle)
where frn.tipo = 2 and cli.NOME like '%NOME DO HOTEL%'
