# 6. Crie um programa que leia três notas (nota1, nota2 e nota3) de um aluno e calcule a média. Se a média for menor do que 5, imprima a mensagem "Reprovado". Se a média for maior ou igual a 5 e menor do que 7, imprima "em recuperação". Se a média for maior ou igual a 7, imprima "Aprovado".

# Solicita ao usuário que insira as três notas como números de ponto flutuante
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Determina a situação do aluno com base na média
if media < 5:
    situacao = "Reprovado"
elif media < 7:
    situacao = "Em recuperação"
else:
    situacao = "Aprovado"

# Exibe a situação do aluno
print(f"A média do aluno é {media:.2f}. Ele está {situacao}.")
