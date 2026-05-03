print(int(1.9456745678)) # Convertendo um número decimal para inteiro, o resultado é 1, pois a parte decimal é descartada
print(int("10")) # Convertendo uma string para inteiro, a string deve conter apenas números, caso contrário, ocorrerá um erro
print(int("10.10")) # Convertendo uma string para inteiro, a string contém um ponto decimal, o que causará um erro, pois não é possível converter uma string com ponto decimal para inteiro
print(float("10.10")) # Convertendo uma string para float, a string deve conter apenas números e um ponto decimal, caso contrário, ocorrerá um erro
print(float("10")) # O resultado é 10.0, pois o número inteiro é convertido para float
print(float(100)) # Convertendo um número inteiro para float, o resultado é 100.0, pois o número inteiro é convertido para um número decimal

valor = 10 # A variável valor é do tipo inteiro, e o valor é 10
valor_str = str(valor) # Convertendo o valor inteiro para string
print(type(valor)) # Imprime o tipo da variável valor, que é <class 'int'>
print(type(valor_str)) # Imprime o tipo da variável valor_str, que é <class 'str'>

print(100 / 2) # O resultado é 50.0 (float), pois a divisão de dois números inteiros resulta em um número decimal
print(100 // 2) # O resultado é 50 (inteiro), pois a divisão inteira descarta a parte decimal e retorna apenas a parte inteira do resultado