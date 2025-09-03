"""
Este arquivo é sobre operações com String em Python.

Strings em Python são sequências de caracteres (imutáveis).
Isso significa que não podemos alterar uma string existente, mas podemos criar novas a partir dela.

==================================================
1) Concatenação de Strings
==================================================
Você pode juntar (concatenar) diferentes textos usando o sinal "+".
"""

name = "João"
print("His name is " + name)  # Concatenação com +

"""
==================================================
2) Concatenação com vírgula no print
==================================================
Usar vírgula dentro do print insere automaticamente um espaço entre os elementos.
"""

print("His name is", name)

"""
==================================================
3) f-strings (formatação moderna)
==================================================
Com 'f' antes da string, você pode inserir variáveis ou expressões
dentro de chaves {}.
"""

print(f"His name is {name}")  # Substitui {name} pelo valor da variável

# Também podemos inserir expressões diretamente:
age = 25
print(f"{name} will be {age + 1} next year.")

"""
==================================================
4) Verificação de substrings
==================================================
Você pode verificar se um trecho de texto está contido em uma string com 'in'.
"""

text = "Python is amazing"
print("Python" in text)     # True
print("java" in text)       # False
print("Python" not in text) # False

"""
==================================================
5) Strings como sequências
==================================================
Podemos acessar caracteres pelo índice (começa em 0).
"""

word = "Python"
print(word[0])  # P
print(word[-1]) # n (última letra)

"""
==================================================
6) Métodos úteis de String
==================================================
As strings têm vários métodos prontos para uso.
"""

sample = "  hello world  "

print(sample.upper())     # "  HELLO WORLD  "
print(sample.lower())     # "  hello world  "
print(sample.title())     # "  Hello World  "
print(sample.strip())     # remove espaços extras: "hello world"
print(sample.replace("world", "Python"))  # substitui: "  hello Python  "
print(sample.split())     # ['hello', 'world']

"""
==================================================
7) Strings multilinha
==================================================
Você pode criar textos grandes com três aspas (duplas ou simples).
"""

multiline = """This is
a text
that spans
multiple lines."""
print(multiline)

"""
==================================================
Resumo
==================================================
- '+' → concatenação
- ',' no print → separa com espaço
- f-strings → interpolação de variáveis/expressões
- 'in' → verificar substring
- [índice] → acessar caracteres
- Métodos úteis: upper(), lower(), title(), strip(), replace(), split()
- Multilinhas → """ """ ou ''' '''
"""
