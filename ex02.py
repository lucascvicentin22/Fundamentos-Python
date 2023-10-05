# 2. Escreva um programa que receba a idade de uma pessoa e verifique se ela é menor de idade (menor que 18 anos) ou maior de idade.

if __name__ == "__main__":


    idade = int(input("Informe a sua idade: "))

    if idade < 21:
        print("Você é ainda menor de idade!")

    else:
        print ("Você ja é maior de idade.")