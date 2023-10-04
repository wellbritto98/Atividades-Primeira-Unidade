
assentos = []
for linhas in range(25):
    assentos.append([])
    for colunas in range(40):
        assentos[linhas].append("💺")

clientes = {nome : " ", assento: " ",qtd_ingressos: 0}
        
def cadastrar_cliente():
    print("\nCadastro do cliente")

    nome = input("Digite o nome: ")
    

def mostrar_assentos():
    for linhas in range(25):
        for colunas in range(40):
            print(assentos[linhas][colunas], end=" ")
        print()
        
def reservar_assento():
    cadastrar_cliente()
    mostrar_assentos()
    print("\nReserva de assento")
    nome_cliente = input("Digite o nome: ")
    lin = int(input("Digite a fileira: "))
    col = int(input("Digite a coluna: "))
    if assentos[lin][col] == "💺":
        assentos[lin][col] = "🔴"
        cadastroDeClientes[nome] = {"nome": nome, "genero": genero}
        qtd_nova_ingressos = clientes[nome_cliente]["qtd_ingressos"] + 1
        clientes[nome_cliente] = {"nome": nome_cliente, "assento": assentos[lin][col], "qtd_ingressos":qtd_nova_ingressos}
        print("\nReserva efetuada com sucesso!")
        mostrar_assentos()
    else:
        print("Assento ocupado!")



reservar_assento()

    
        
        
