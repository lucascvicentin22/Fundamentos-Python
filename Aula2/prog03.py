"""
ESTRUTURA DE REPETIÇÃO 

LAÇO WHILE

o 'WHILE' É A SEGUNDA ESTRUTURA DE CONTROLE DE REPETIÇÃO DO PYTHON. SEMELHANTE AO 
LAÇO FOR, O O LAÇO 'WHILE' VAI EXECUTAR UM CLOCO DE CÓDIGO ENQUANTO UMA DADA
EXPRESSÃO FOR VERDADEIRA.

"""
# Importar a função randint do módulo random, que faz parte da biblioteca padrão do python

from random import randint

if __name__ == "__main__": 
    
    # Exemplo: Incrementar um número até um limite

    numero = 0

    while numero < 10:
        print(numero)
        numero += 1

    # Assim como no laço for, podemos utilizar os comandos break e continue dentro de
    # um laço while

    
    lista_numeros = []

    # while True significa que nosso loop infinito, a não ser que seja interrompido
    # por um comando break

    while True:

        # Se´r agerado um número randomico entre -5 e 20, e será atribuido à variável
        # numero 
        numero = randint(-1, 20)

        if numero < 0:
            print(f"Foi gerado um número negativo({numero}). Saindo.")
            break

            # O método append adiciona um novo elemento no final da lista
            lista_numeros.append(numero)

    # a função build-in sum() soma os números de uma sequência (lista, tuple, etc)        

    print(f"Soma : {sum(lista_numeros)}")

    # Assim como no laço for, também podemos utilizar o comando continue dentro do laço while

    lista_tipos = [
        2, 5, 4.7, 4.1, 2.3,
        "Python", "C#" , "Proway",
        [1, 2, 3], ['a', 'b' , 'c'],
        4, 5.5, 8.4
    ]

# O método clear() limpa a lista, ou seja, exclui todos os seus valores
lista_numeros.clear()

contador = 0

# Exemplo: Adiciona apenas valores numéricos a uma lista

while contador < len(lista_tipos):

    valor_atual = lista_tipos[contador]
    if not isinstance(valor_atual, int) and not isinstance(valor_atual, float):
        print(f"O valor {valor_atual} não é do tipo numerico. Ignorando...")
        contador += 1
        continue

    lista_numeros.append(valor_atual)
    contador += 1

    # Ah sim como no laço for, também conseguimos utilizar else no laço while
    # O bloco else não será executado se o comando break for executado dentro do bloco
    contador = 0

    while contador < 10:
        contador += 1

        #if contador > 8:
        #    break

    else:
        print(f"Valor final do contador: {contador}")