# ============================================================
# ATIVIDADE: Calculadora de Produtos
# Tema: Operadores Aritméticos e Precedência de Operadores
# ============================================================

# -------------------------------------------------------
# PARTE 1 — Operadores Aritméticos
# -------------------------------------------------------
# Considere dois produtos com os seguintes preços:

produto_1 = 45
produto_2 = 12

# Calcule e exiba no console:
# 1. A soma dos dois preços
print(produto_1 + produto_2)
# 2. A diferença entre o preço do produto_1 e do produto_2
print(produto_1 - produto_2)
# 3. A divisão do produto_1 pelo produto_2 (com casas decimais)
print(produto_1 / produto_2)
# 4. A divisão inteira do produto_1 pelo produto_2
print(produto_1 // produto_2)

# 5. O produto (multiplicação) dos dois preços
print(produto_1 * produto_2)
# 6. O resto da divisão do produto_1 pelo produto_2
print(produto_1 % produto_2)
# 7. O resultado de elevar o produto_1 à potência de 2
print(produto_1 ** 2)

# -------------------------------------------------------
# PARTE 2 — Precedência de Operadores
# -------------------------------------------------------
# Antes de rodar o código, escreva qual resultado você espera
# para cada expressão e explique qual operador foi executado
# primeiro e por quê. Depois execute e compare.

a = 8 + 3 * 2
b = (8 + 3) * 2
c = (100 // 5) + (3 ** 3) - (15 % 4)

# Exiba os valores de a, b e c
print(a) # O resultado será 14, pois a multiplicação tem precedência sobre a adição, então o resultado será 8 + (3 * 2) = 8 + 6 = 14
print(b) # O resultado será 22, pois os parênteses têm precedência sobre a multiplicação, então o resultado será (8 + 3) * 2 = 11 * 2 = 22
print(c) # O resultado será 30.0, pois a divisão e exponenciação são executadas primeiro, depois a adição e subtração.
print(a, b, c, s , sep="|", end="|\n")
# -------------------------------------------------------
# PARTE 3 — Desafio
# -------------------------------------------------------
# Crie duas expressões aritméticas próprias utilizando
# no mínimo quatro operadores diferentes em cada uma.
# Explique a ordem de execução com comentários usando #.

# Expressão 1:
expressao_1 = 10 + 5 * 2 - 8 / 4
# Explicação: A multiplicação e divisão são executadas primeiro, depois a adição e subtração.

# Expressão 2:
expressao_2 = (15 % 4) ** 2 + 10 // 3
# Explicação: O módulo e a exponenciação são executados primeiro, depois a divisão inteira e a adição.
print(expressao_1)
print(expressao_2)