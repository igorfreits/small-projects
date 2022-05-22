"""
List Comprehension - Hastag
"""
# Tudo em um alinha código
# Mais rápido e "simples"

# list_comprehension EXEMPLO = ["item"(variável) (condição/operação) PARA CADA "item" SE a condição for verdadeira]
#                                                                     for in         if

lista_preços = [500, 1500, 2000, 100, 25]
nova_lista_de_preços = []

# Dobrar valor
for preço in lista_preços:
    nova_lista_de_preços.append(preço * 2)
print(nova_lista_de_preços)

# Para cada "item" na minha lista adicione "item" * 2
nova_lista_de_preços = [
    preço * 2 for preço in lista_preços]  # List comprehension
print(nova_lista_de_preços)

print()

# produtos acima de 1000 dolares + 50% do valor total
imposto2 = []
for preço in lista_preços:
    if preço > 1000:
        imposto2.append(preço * 0.5)
print(imposto2)

print()

# Para cada "item" acima se 1000...adicione + 50%
imposto2 = [preço * 0.5 for preço in lista_preços if preço > 1000]
print(imposto2)
