"""
Este arquivo é sobre condicionais em Python.

==================================================
1) Estrutura básica do if/elif/else
==================================================
Em Python, usamos condicionais para executar blocos de código
apenas se certas expressões forem verdadeiras.

IMPORTANTE: O código deve estar indentado (recuado com 4 espaços).

Sintaxe:
if condição:
    # código executado se condição for True
elif outra_condição:
    # código se a primeira for False e esta True
else:
    # código se nenhuma condição for verdadeira
"""

numA = 1
numB = 2

conditionA = numA > numB
conditionB = numB > numA

if conditionA:
    print("ConditionA true")
elif conditionB:
    print("ConditionB true")
else:
    print("None of conditions are true")

"""
==================================================
2) Operadores relacionais
==================================================
- Maior ............ >
- Menor ............ <
- Maior ou igual ... >=
- Menor ou igual ... <=
- Igualdade ........ ==
- Diferença ........ !=
"""

x = 10
y = 20
print(x == y)  # False
print(x != y)  # True
print(x >= 10) # True

"""
==================================================
3) Operadores lógicos
==================================================
- AND → True se ambas as condições forem verdadeiras
- OR  → True se pelo menos uma condição for verdadeira
- NOT → inverte o valor lógico
"""

a = 5
b = 8

if a > 0 and b > 0:
    print("Both are positive")

if a < 0 or b > 0:
    print("At least one is positive")

if not (a > b):
    print("a is NOT greater than b")

"""
==================================================
4) If aninhado (nested if)
==================================================
Um if dentro de outro.
"""

n = 15
if n > 0:
    if n % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")

"""
==================================================
5) Operador ternário
==================================================
Permite escrever um if/else em uma única linha.
"""

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # → "Adult"
