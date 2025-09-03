"""
Este arquivo é sobre manipulação de Strings em Python.

==================================================
1) Índice e tamanho
==================================================
- Strings são sequências, logo podemos acessar caracteres por índice.
- O índice começa em 0 (primeiro caractere).
- O tamanho pode ser obtido com len().
"""

text = "Python"

print(text[0])   # P (primeiro caractere)
print(text[1])   # y
print(text[-1])  # n (último caractere)

print(len(text)) # 6 (número de caracteres)

"""
==================================================
2) Slices (cortes de string)
==================================================
Podemos extrair partes de uma string usando a notação [início:fim:passo].

- início: índice inicial (inclusivo)
- fim: índice final (exclusivo)
- passo: salto entre índices
"""

word = "programming"

print(word[0:7])   # "program" (do índice 0 ao 6)
print(word[:7])    # "program" (mesmo que acima, início implícito)
print(word[3:])    # "gramming" (do índice 3 até o fim)
print(word[::2])   # "pormig" (de 2 em 2)
print(word[::-1])  # "gnimmargorp" (string invertida)

"""
==================================================
3) Operações com strings
==================================================
- Concatenação: usar +
- Repetição: usar *
- Verificar substring: 'in' / 'not in'
"""

a = "Hello"
b = "World"

print(a + " " + b)  # "Hello World"
print(a * 3)        # "HelloHelloHello"
print("Hell" in a)  # True
print("bye" not in a) # True

"""
==================================================
4) Métodos úteis de string
==================================================
"""

sample = "  Python is FUN!  "

print(sample.lower())   # "  python is fun!  "
print(sample.upper())   # "  PYTHON IS FUN!  "
print(sample.title())   # "  Python Is Fun!  "
print(sample.strip())   # remove espaços extras: "Python is FUN!"
print(sample.replace("FUN", "powerful"))  # substitui texto
print(sample.split())   # ["Python", "is", "FUN!"]

# Verificações
print(sample.startswith("  Py"))  # True
print(sample.endswith("!  "))     # True
print("123".isdigit())            # True
print("abc".isalpha())            # True
print("abc123".isalnum())         # True

"""
==================================================
5) Formatação de números em strings
==================================================
Podemos formatar números em strings usando f-strings
ou o método format().
"""

pi = 3.14159265
num = 1234

print(f"Pi with 2 decimals: {pi:.2f}")        # 3.14
print(f"Number with commas: {num:,}")         # 1,234
print(f"Percentage: {0.85:.0%}")              # 85%

# Usando .format()
print("Pi = {:.3f}".format(pi))               # 3.142

"""
==================================================
Resumo
==================================================
- Índices e len() → acesso e tamanho
- Slices → cortes flexíveis
- Operações: +, *, in, not in
- Métodos: lower(), upper(), strip(), replace(), split(), etc.
- Formatação → f-strings e format()
"""
