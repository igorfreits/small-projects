"""A abs()função retorna o valor absoluto do número fornecido.
Se o número for um número complexo, abs()retorna sua magnitude.

Exemplo"""
number = -20.6

absolute_number = abs(number)
print(absolute_number)  # Output: 20
# int,float,complex number

"""A any()função retorna True
se algum elemento de um iterável for True. Se não, ele retorna False.

Exemplo"""
boolean_list = ['True', 'False', 'True']

# verifica se algum elemento é verdadeiros
result = any(boolean_list)
print(result)  # Output: True
# iterável (lista, string, dicionário etc.)

"""A all()função retorna True
se todos os elementos no iterável fornecido forem verdadeiros.
Se não, ele retorna False.

Exemplo"""
boolean_list = ['True', 'True', 'True']

# verifica se todos os elementos são verdadeiros
result = all(boolean_list)
print(result)  # Output: True
# iterável (lista, string, dicionário etc.)

"""O ascii()método substitui um caractere não imprimível
por seu valor ascii correspondente e o retorna.

Exemplo"""
text = 'Pythön is interesting'

# substitui ö pelo seu valor ascii
print(ascii(text))  # Output: 'Pyth\xf6n is interesting'
# object (list, set, tuple, etc)
