if __name__ == "__main__":
    
    #numero1 = input ("Informe o primeiro número: ")
   # numero2 = input ("Informe o segundo número: ")

   # print ("A soma de " + numero1 + " e " + numero2 + " é igual a " + numero1 + numero2)

    #Convertendo o valor string para Int numeros inteiros com o metodo format
    #numero1 = int(numero1)
    #numero2 = int(numero2)

    #print("A soma de {} e {} é igual a {}". format(numero1, numero2, numero1 + numero2))

    # Convertendo string para tipo float() Numeros quebrados

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    media = (nota1 + nota2 + nota3) /3

    # Podemos formatar o valor de saida dos numeros,
    # :.2f significa que após o ponto, vão ser mostradas no maximo 2 casas decimais

    print("A média final é de {:.1f}".format(media))