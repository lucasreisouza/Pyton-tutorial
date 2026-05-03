# Exercício: Ficha de Produto
# Você trabalha em um sistema de cadastro de produtos. Escreva um programa em Python que solicite ao usuário o nome do produto e o preço, e exiba essas informações de quatro formas diferentes:

# Exiba o nome e o preço separados por espaço (comportamento padrão).
# Exiba o nome e o preço separados por espaço, mas finalizando a linha com  <<< seguido de uma quebra de linha.
# Exiba o nome e o preço separados por |, finalizando com  <<< e uma quebra de linha.
# Exiba o nome e o preço separados por |, usando a quebra de linha padrão.

# Exemplo de saída esperada (para produto "Caneta" e preço "2.50"):
# Caneta 2.50
# Caneta 2.50 <
# Caneta | 2.50 <
# Caneta | 2.50

produto = input("Informe o nome do produto: ")
preco = input("Informe o preço do produto: ")

print(produto, preco)
print(produto, preco, end=" <<<\n")
print(produto, preco, sep="|", end=" <<<\n")
print(produto, preco, sep="|")