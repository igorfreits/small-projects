"""
Dicionários
"""


emails_gerentes = {
    'Iguatemi': 'iguatemi@gmail.com',
    'Plaza': 'plaza@hotmail.com',
    'Barra': 'barra@gamil.com',
}


print(emails_gerentes['Barra'])
email = emails_gerentes['Iguatemi']
print(email)

# Adiciona um novo item
emails_gerentes['Leblon'] = 'leblon@gmail.com'
#                 chave          valor
print(emails_gerentes)
# Se o valor ou ja existir ele irar substituir


# Para cada "item no meu dicionário"
for shopping in emails_gerentes:  # Iterável
    print(shopping)

print(emails_gerentes.keys())  # Exibi as chaves do dicionário


for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)

print(emails_gerentes.values())  # Exibi os valores das chaves

emails_gerentes.pop('Leblon')  # remove a chave escolhida
print(emails_gerentes)

# Verifica se um Shopping Existe
if 'Iguatemi' in emails_gerentes:
    print('Existe')
else:
    print('Nao existe')
