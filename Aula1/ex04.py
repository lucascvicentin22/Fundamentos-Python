# 4. Crie um programa que peça ao usuário para digitar dois números inteiros e exiba a soma, subtração, multiplicação e divisão dos números.

# Solicita ao usuário para digitar dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Calcula a soma, subtração, multiplicação e divisão dos números
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Certifique-se de evitar a divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero"

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
