"""
Este arquivo é sobre operações matemáticas em Python.

SUM (+)
SUBTRACTION (-)
DIVISION (/)
MULTIPLICATION (*)
POWER (**)
REMAIN (%)

Python will follow the same order of operations as math.
=======
==================================================
1) Operadores matemáticos básicos
==================================================
- SOMA ............. +
- SUBTRAÇÃO ........ -
- MULTIPLICAÇÃO .... *
- DIVISÃO .......... /
- POTÊNCIA ......... **
- RESTO (módulo) ... %
- DIVISÃO INTEIRA .. //

Python segue a mesma ordem de precedência da matemática:
1) Potências e raízes
2) Multiplicação, divisão, divisão inteira e módulo
3) Soma e subtração
(Parênteses podem alterar a ordem).
>>>>>>> 80cab98 (basic content)
"""

# Exemplos básicos
print(1 + 2)    # soma → 3
print(54 - 8)   # subtração → 46
print(100 / 10) # divisão (sempre retorna float) → 10.0
print(3 * 4)    # multiplicação → 12

# Potência
print(2 ** 10)  # 2 elevado a 10 → 1024

# Resto da divisão
print(10 % 3)   # 10 dividido por 3 deixa resto 1

# Divisão inteira (descarta a parte decimal)
print(10 // 3)  # resultado → 3

"""
==================================================
2) Ordem de operações
==================================================
Assim como na matemática, a precedência é respeitada.
"""

print(1 + 2 ** 2)     # 1 + (2**2) → 1 + 4 = 5
print((1 + 2) ** 2)   # (1+2) ** 2 → 3**2 = 9
print(2 * 2 ** 2)     # 2 * (2**2) = 2*4 = 8
print((2 * 2) ** 2)   # (2*2)**2 = 4**2 = 16

print(1+2**2)
print((1+2)**2)
print(2*2**2)
print((2*2)**2)
"""
==================================================
3) Números negativos e floats
==================================================
Python lida normalmente com negativos e decimais (float).
"""

print(-5 + 3)    # → -2
print(3.5 * 2)   # → 7.0
print(7 / 2)     # → 3.5
print(7 // 2)    # → 3 (descarta a parte decimal)

"""
==================================================
4) Atenção com precisão em floats
==================================================
Números decimais em Python seguem a representação binária,
podendo gerar pequenas imprecisões.
"""

print(0.1 + 0.2) # → 0.30000000000000004

"""
==================================================
5) Biblioteca math
==================================================
A biblioteca 'math' fornece funções matemáticas adicionais,
como raiz quadrada, arredondamento, seno, cosseno, logaritmos etc.

Exemplo (não vamos explorar, neste momento, em detalhes):
"""

import math
print(math.sqrt(16))  # → 4.0 (raiz quadrada)
print(math.pi)        # → 3.141592653589793
print(math.factorial(5)) # → 120
