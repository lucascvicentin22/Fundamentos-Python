# 5. Escreva um programa que solicite o nome, a idade e o sexo do usuário. Em seguida, exiba uma mensagem personalizada informando se o usuário é homem ou mulher e se é maior ou menor de idade.

# Solicita ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicita ao usuário que insira sua idade como um número inteiro
idade = int(input("Digite sua idade: "))

# Solicita ao usuário que insira seu sexo (M para masculino, F para feminino)
sexo = input("Digite seu sexo (M para masculino ou F para feminino): ")

# Verifica o sexo e a idade para exibir a mensagem apropriada
if sexo == "M" or sexo == "m":
    genero = "homem"
else:
    genero = "mulher"

if idade >= 18:
    situacao_idade = "maior de idade"
else:
    situacao_idade = "menor de idade"

# Exibe a mensagem personalizada
print(f"Olá, {nome}! Você é um {genero} e é {situacao_idade}.")
