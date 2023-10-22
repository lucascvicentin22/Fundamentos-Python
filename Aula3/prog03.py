"""
Estrutura de dados em python

Sets (conjuntos)

Um set é uma estrutura de dados que armazena um conjunto de valores. Sets não são 
ordenados, não são indexáveis, são imutáveis e não permitem valores repetidos.

* Apenas de não conseguirmos alterar um valor existente, podemos adicionar ou remover valores

"""


from random import randint

if __name__ == "__main__": 

    # Criação de um set

    conjunto_a = {1,2,3,4,5}

    conjunto_b = set([5,4,3,2,1])

    print(conjunto_a, conjunto_b)

    try:

        # A linha abaixo irá gerar um exceção do tipo TypeError
        print(conjunto_a[0])

    except:
        print("Sets não são indexáveis.")

    #Criando a lista de números aleatórios da maneira classica
    lista_numero = []

    # A função range() gerá uma sequência de números. No caso abaixo, de 0 até 98
    for numero in range(100):
        lista_numero.append(randint(1,50))

        print(lista_numero)
    
    # Criando a lista de números utilizando list comprehension
    # Quando não utilizamos uma variável, mas ela é necessária pra sintaxe da expressão,
    # podemos troc-la pelo underline(_)
    lista_numero = [randint(1,50) for _ in range(100)]
    print(f"Tamanho: {len(lista_numero) } |", lista_numero)

    # Removendo os valores repetidos, Para isso, vamos converter a lista para um set e 
    # converter esse set para uma lista.

    lista_numero = list(set(lista_numero))
    print(lista_numero)