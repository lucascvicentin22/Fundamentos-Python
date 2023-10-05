# 7. Faça um programa que receba uma temperatura em graus Celsius e exiba a temperatura equivalente em graus Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.

# Solicita ao usuário que insira a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Calcula a temperatura em graus Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe a temperatura em graus Fahrenheit
print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}°F.")
