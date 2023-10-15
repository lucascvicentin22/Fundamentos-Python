# 3. Escreva um programa que leia três números inteiros e exiba o maior e o menor deles.
if __name__ == "__main__":

  # Solicita ao usuário que insira três números inteiros
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))

    # Inicializa as variáveis para armazenar o maior e o menor número
    maior_numero = numero1
    menor_numero = numero1

    # Verifica se o segundo número é maior ou menor
    if numero2 > maior_numero:
        maior_numero = numero2
    elif numero2 < menor_numero:
        menor_numero = numero2

    # Verifica se o terceiro número é maior ou menor
    if numero3 > maior_numero:
        maior_numero = numero3
    elif numero3 < menor_numero:
        menor_numero = numero3

    # Exibe o maior e o menor número
    print(f"O maior número é {maior_numero}")
    print(f"O menor número é {menor_numero}")
