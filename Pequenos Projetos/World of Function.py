"""A abs()função retorna o valor absoluto do número fornecido.
Se o número for um número complexo, abs()retorna sua magnitude.
Exemplo"""
number = -20.6
absolute_number = abs(number)  # numero absoluto
print(absolute_number)  # Output: 20
# int,float,complex number

"""A any()função retorna True
se algum elemento de um iterável for True. Se não, ele retorna False.
Exemplo"""
boolean_list = ['True', 'False', 'True']  # Lista de booleans
# verifica se algum elemento é verdadeiros
result = any(boolean_list)
print(result)  # Output: True
# iterável (lista, string, dicionário etc.)

"""A all()função retorna True
se todos os elementos no iterável fornecido forem verdadeiros.
Se não, ele retorna False.
Exemplo"""
boolean_list = ['True', 'True', 'True']  # Lista de booleans
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

"""O bin()método converte um número inteiro especificado
em sua representação binária e o retorna.
Exemplo"""
number = 15
# converte 15 para seu equivalente binário
print('The binary equivalent of 15 is', bin(number))
# Output: The binary equivalent of 15 is 0b1111
# int

"""O bool()método recebe um argumento especificado
e retorna seu valor booleans.
Exemplo"""
test = 1
# retorna valor booleans de 1
print(test, 'is', bool(test))  # Output: 1 is True
# Argumento cujo valor booleans é retornado

"""O bytearray()método retorna um objeto bytearray que
é uma matriz dos bytes fornecidos.
Exemplo"""
prime_numbers = [2, 3, 5, 7]  # NUmero primos
# converter lista para bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)  # Output: bytearray(b'\x02\x03\x05\x07')
"""
source (Opcional) - source para inicializar o array de bytes.
codificação (Opcional) - se a fonte for uma string, a codificação da string.
erros (opcional) - se a fonte for uma string, a ação a ser
tomada quando a conversão de codificação falhar
"""

"""O método callable() retorna True se o objeto passado parecer chamavel.
Se não, retorna False.
A sintaxe de callable()é:"""
# callable(objeto)
x = 5
print(callable(x))  # False


def testFunction():
    print("Test")


y = testFunction
print(callable(y))  # Tru
# argumento

"""O bytes()método retorna um objeto de bytes imutável
inicializado com o tamanho e os dados fornecidos.
Exemplo"""
message = 'Python is fun'
# converte string em bytes
byte_message = bytes(message, 'utf-8')
print(byte_message)  # Output: b'Python is fun'
"""
source (Opcional) - source para inicializar o array de bytes.
codificação (Opcional) - se a fonte for uma string, a codificação da string.
erros (opcional) - se a fonte for uma string, a ação a ser
tomada quando a conversão de codificação falhar
"""

"""O chr()método converte um inteiro em seu caractere unicode e o retorna.
Exemplo"""
print(chr(97))  # Output: a
print(chr(98))  # Output: b
# um número inteiro no intervalo de 0 a 1.114.111

"""O método compile() retorna um objeto de código Python da fonte
(string normal, uma string de bytes ou um objeto AST).
A sintaxe de compile()é:"""
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)  # soma = 11
"""compile()O método é usado se o código Python estiver na forma de string
ou for um objeto AST e você quiser alterá-lo para um objeto de código.
O objeto de código retornado pelo compile()método pode ser
chamado posteriormente usando métodos como: exec() e eval()
que executarão código Python gerado dinamicamente."""
"""
source- uma string normal, uma string de bytes ou um objeto AST
filename- arquivo do qual o código foi lido.
Se não foi lido de um arquivo, você mesmo pode dar um nome
mode- Ou exec ou eval ou single.
eval- aceita apenas uma única expressão.
exec- Pode receber um bloco de código que tenha instruções,
classes e funções Python, e assim por diante.
single- se consiste em uma única instrução interativa
flags(opcional) e dont_inherit(opcional) - controla quais declarações futuras
afetam a compilação da fonte. Valor padrão: 0
optimize(opcional) - nível de otimização do compilador. Valor padrão -1."""

"""O classmethod()método retorna um método de classe para a função fornecida.
Exemplo"""


class Student:
    marks = 0

    def compute_marks(self, obtained_marks):
        marks = obtained_marks
        print('Obtained Marks:', marks)


# converter compute_marks() para o método de classe
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)  # Output: Obtained Marks: 88
# função - Função que precisa ser convertida em um método de classe

"""O método complex() retorna um número complexo quando partes reais e
imaginárias são fornecidas, ou converte uma string em um número complexo.
A sintaxe de complex()é:"""
# complex([real[, imagem]])
z = complex(2, -3)
print(z)  # (2-3j)

z = complex(1)
print(z)  # (1+0j)

z = complex()
print(z)  # 0j

z = complex('5-9j')
print(z)  # (5-9j)
"""real - parte real/imag - parte imaginária.(Se for omitido, o padrão é 0.)
Se o primeiro parâmetro passado para este método for uma string,
ela será interpretada como um número complexo. Neste caso,
o segundo parâmetro não deve ser passado.
"""

"""O delattr() exclui um atributo do objeto (se o objeto permitir).
A sintaxe de delattr()é:"""

# delattr(objeto, nome)


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# Raises Error
#print('z = ', point1.z)
# objeto - o objeto do qual nome atributo deve ser removido
# name - uma string que deve ser o nome do atributo a ser removido do objeto

"""O construtor dict() cria um dicionário em Python.
Diferentes formas de dict()construtores são:"""
# classe dict(**kwarg)
# class dict(mapeamento, **kwarg)
# class dict (iterável, ** kwarg)
numbers = dict(x=5, y=0)
print('numbers =', numbers)  # números = {'y': 0, 'x': 5}
print(type(numbers))  # <class 'dict'>

empty = dict()
print('empty =', empty)  # vazio = {}
print(type(empty))  # <class 'dict'>
