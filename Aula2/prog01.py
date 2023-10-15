"""
MATCH CASE

MATCH CASE PODE SER ENTENDIDA COMO A ESTRUTURA SWITCH CASE NO PYTHON. ELA É USADA 
QUANDO QUEREMOS ESCOLHER UM VALOR DENTRE VALORES POSSIVEIS

"""

usuario = 1
moderador = 2
admistristrador = 3

if __name__ == "__main__": 
    valor = int(input("informa a permissão do usuário: "))

    match valor :
        case 1 :
            print("Identificado como Usuário. Permissões comuns.")

        case 2 :
            print("Identificamos como Moderador. Você pode moderar Menssagns e Usuário.")

        case 3 :
            print("Identificamos como Administrador. Você possui acesso total. ")

            #Case padrão . Se nenhum das comparações anteriores retorem True
        case _:
            print("Permissão desconhecida, Sem informações.")