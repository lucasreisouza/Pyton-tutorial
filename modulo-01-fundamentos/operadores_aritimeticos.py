produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)  # Soma
print(produto_1 - produto_2)  # Subtração
print(produto_1 / produto_2)  # Divisão
print(produto_1 // produto_2)  # Divisão inteira
print(produto_1 * produto_2)  # Multiplicação
print(produto_1 % produto_2)  # Módulo
print(produto_1 ** produto_2)  # Potência

x = 10 + 5 * 4 # A multiplicação tem precedência sobre a adição, então o resultado será 10 + (5 * 4) = 10 + 20 = 30
y = (10 / 2) + (25 * 2) - (2 ** 2) # A multiplicação e a divisão têm precedência sobre a adição e subtração, então o resultado será (10 / 2) + (25 * 2) - (2 ** 2) = 5 + 50 - 4 = 51
print(x) # O resultado será 30
print(y) # O resultado será 51