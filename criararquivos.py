def criar_arquivos():
    arquivo = input("Digite o nome do arquivo: ")
    tipo = input("Digite o tipo do arquivo(.txt, .csv, .xls): ")
    arquivo = arquivo + tipo
    arquivo = open(arquivo, "w")

while True:
    print("\n1 - Criar arquivo")
    print("Whatever - Sair")
    opcao = int(input("\nDigite a opção: "))
    
    if opcao == 1:
        criar_arquivos()
    else:
        break        