"""

ESTRUTURA DE DADOS EM PYTHON

LISTA

UMA LISTA É UM DOS TIPOS DE ESTRUTURAS DE DADOS PYTHON. ELA TEM AS SEGUINTES CARACTERISTICAS: 
SER ORDENADA, MUTÁVEL, INDEXÁVEL E PERMITIR VALORES REPETIDOS.

"""

if __name__ == "__main__":

    #Lista podem ser criadas das seguintes maneiras: 

    lista = []                          #Lista vazia    
    lista = [1, 2, 3]                   #Lista criada com valores
    lista = list()                      #Utilizando a função list()
    lista = list("Python")              #Passando um objeto iterável para a lista


    # Lista em Python são ordenadas, ou seja, elas vão manter a ordem dos itens no momento 
    # de sua criação
    print(lista)


    # Também são mutáveis, ou seja, podemos alterar qualquer item na lista
    lista[0] = "a"          # ALteramos o valor do indice 0
    print(lista)

    # Também são indexáveis, ou seja, podemos acessar qualquer valor da lista a partir 
    #do indice
    print(lista[3])

    """
    OS INDICES DE UMA LISTA EM PYTHON FUNCIONAM DA SEGUINTE MANEIRA:
    LINGUAGENS = ["PYTHON", "C#", "JAVA" , "JAVASCRIPT" , "GOLANG"]
                    0         1      2          3             4
                    -5        -4     -3         -2            -1
        VEMOS ACIMA QUE TAMBÉM PODEMOS ATILIZAR INDICES NEGATIVOS NA NOSSA LISTA, COMENÇANDO
        DO FINAL COM -1
    """    

    # Pegando a penúltima letra da lista
    print(lista[-2])

    # Por último, uma lista ter valores repetidos
    lista = ["Proway", "Blumenau", "Blumenau"]
    print(lista)


    """
    FATIAMENTO DE LISTAS EM PYTHON

    EM PYTHON, PODEMOS FAZER O 'SLICING' (FATIAMENTO) DE LISTAS, QUE NADA SÃO MAIS DO QUE 
    EXTRAIRMOS PEDAÇOS DE UMA LISTA, A PARTAR DOS SEUS INDICES. NOTE QUE QUANDO UTILIZAMOS O 
    FATIAMENTO, UMA NOVA LISTA É CRIADA.

    SINTAXE: [START: STOP:STEP]

    START (OPCIONAL): INDICE DE INICIO INCLUSIVO
    STOP (OPCIONAL): INDICE DE FIM EXCLUSIVO
    STEP (OPCIONAL): DE QUANTOS EM QUANTOS ITENS SERÃO EXTRAIDOS
    """


    linguagens = ["PYTHON", "C#", "JAVA" , "JAVASCRIPT" , "GOLANG", "PHP", "SQL"]


    # Exemplo: "Fatiar" a lista extraindo os valores "Java" e "Javascript"
    print(linguagens[2:4])

    # Exemplo 2: Pegar todos os itens da lista, pulando de 2 em 2
    print(linguagens[1::2])

    # Exemplo 3: Utilizando indices negativos no slice
    print(linguagens[:-1:2])

    # Métodos de lista em Python
    # Metodos de remoção de itens
    # Remove um item de uma lista a partir do seu valor. Caso exita mais um 1 itemcom o mesmo
    # valor, a primeira ocorrência encontrada da esquerda para a direita é removida

    linguagens.remove("SQL")
    print(linguagens)


    #Pop(indice)
    # Remove e retorna um item de uma lista a partir do indice informado. Se não for informad
    #um indice, retorna o último elemento da lista
    print(f"Removendo '{linguagens.pop(2)}' da lista")
    print(linguagens)


    # Comando del
    # Podemos remover um item da lista utilizando esse comando
    del linguagens[-1]
    print(linguagens)


    # Clear()
    # Apaga todos os itens da lista
    linguagens.clear()
    print(linguagens)

    # Metodos de adição de elementos

    #Append(item)
    #Insere um item no final de um lista
    linguagens.append("Python")
    print(linguagens)

    #Extend(sequencia)
    # Extende os itens de uma lista com os itens da sequência informada
    tupla_linguagens = ("C#", "Javascript", "SQL",)
    linguagens.extend(tupla_linguagens)
    print(linguagens)

    # Insert(posição, valor)
    linguagens.insert(-1, "Golang")
    print(linguagens)

    #Também podemos concatenar uma lista com a outra
    linguagens += ["Perl", "Haskell"]
    print(linguagens)