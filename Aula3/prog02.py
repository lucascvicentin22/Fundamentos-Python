"""
Estruturas de dados em Python

Tuplas

Tuplas são bastantes semelhante4s a listas, ou seja, são indexáveis, iteráveis e 
armazenam qualquer tipo de dados. A principal diferença é que tuplas são imutaveis, ou seja, 
depois de criadas não podem ter os seus valores alterados.

"""

if __name__ == "__main__": 
    # Criação de tuplas
    tupla = ("Python", "JavaScript", "C#")
    print(tupla)
    tupla = tuple("Python")
    print(tupla)

    # Como dito, não podemos alterar um valor de uma tupla ja criada. A linha abaixo dará erro
    #tupla[2] = "Golang"

    # Caso mesmo assim seja necessário alterar o valor de uma tupla, podemos utilizar a 
    #seguinte estratégia: 

    #Criamos uma nova lista a partir da tupla
    lista = list(tupla)

    #alteramos o item desejado
    lista[2] = "Golang"

    #Convertemos novamente a lista em uma tupla
    tupla = tuple(lista)

    print(tupla)