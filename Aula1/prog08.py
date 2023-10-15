# Laço de condição if... elif...else

if __name__ == "__main__":
    """
    O laço if... else... elif faz parte das bases de qualquer linguagem de programação. Com ele posssamos ferificar
    valores e condições que façam parte qualquer algoritimos. por isso o seu entendimento é fundamental.

    """
    # Quando criamos variaveis com todas as latras em maiuculo dentro do Python, indicamos que 
    # que essas variaveis devem ser tratadas
    # como o python não possui uma palavra reserveda para garantir que o valor não seja alterado (const no C#, por exemplo),
    # isso faz parte das convenções de código do python.

    VISITANTE = 1
    USUARIO = 2
    ADMIN = 3
    
    mensagem = """

    Bem Vindo. Informe o código do tipo de usuário para continuar
    Visitante (1) - Usuario (2) - Admintrador (3)
    """

    print(mensagem)

    codigo = int(input("Informe o codigo: "))

    if codigo == VISITANTE:
        print("Identificado como visitante. Acesso somante leitura")

    elif codigo == USUARIO:
        print("Identificamos como Usuário. Permissões comuns no sistema ")

    elif codigo == ADMIN:
        print("Identificamos como adminstrador. Permissão total de acesso")

    else:
        print("Código de usuário desconhecido. Sem permissões")