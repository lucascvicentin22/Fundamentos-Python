# 10. Escreva um programa que leia o salário de um funcionário e exiba o valor do salário líquido, descontando o INSS. As faixas de desconto são as seguintes:
#* Até R$ 1.320,00                   7,5%
#* De R$ 1.320,01 a R$ 2.571,29 	    9%
#* De R$ 2.571,30 até R$ 3.856,94 	12%
#* Acima de R$ 3.856,95              14%

# Solicita ao usuário que insira o salário do funcionário
salario_bruto = float(input("Digite o salário bruto do funcionário: "))

# Calcula o desconto do INSS com base nas faixas de desconto
if salario_bruto <= 1320.00:
    inss_desconto = salario_bruto * 0.075
elif salario_bruto <= 2571.29:
    inss_desconto = salario_bruto * 0.09
elif salario_bruto <= 3856.94:
    inss_desconto = salario_bruto * 0.12
else:
    inss_desconto = salario_bruto * 0.14

# Calcula o salário líquido (salário bruto - desconto do INSS)
salario_liquido = salario_bruto - inss_desconto

# Exibe o salário líquido
print(f"O salário líquido do funcionário é R${salario_liquido:.2f}.")
