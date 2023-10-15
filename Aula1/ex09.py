# 9. Crie um programa que receba o nome, o peso e a altura de uma pessoa. Em seguida, calcule o seu IMC. A altura deve ser informada no formato `metros.centimetros` (exemplo 1.79). A fórmula do IMC é a seguinte: peso / (altura * altura).

# Solicita ao usuário que insira o nome, peso e altura
nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros, por exemplo, 1.79): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC
print(f"Olá, {nome}! Seu IMC é {imc:.2f}.")
