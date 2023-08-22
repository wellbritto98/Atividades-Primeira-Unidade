import random
import string

# region Area de métodos
def ValidaNome(nome):
    return nome.isalpha()

def ValidaGenero(genero):
    return genero.upper() in ["M", "F", "NB"]

def ValidaNumero(num):
    return num.isdigit()

def InserirCliente():
    nome = input("Digite o nome do cliente: ")
    while not ValidaNome(nome):
        print("Nome inválido. Por favor, insira um nome sem números.")
        nome = input("Digite o nome do cliente: ")

    genero = input("\nGenero do cliente \nM - Masculino, \nF - Feminino, \nNB - Não Binario:\n").upper()
    while not ValidaGenero(genero):
        print("Genero inválido. Selecione M, F ou NB.")
        genero = input("Qual genero do cliente (M, F, NB): ").upper()

    cadastroDeClientes[nome] = {"nome": nome, "genero": genero}
    print(f"\n Cliente {nome} cadastrado ")

def PesquisarCliente():
    nome = input("Digite o nome do cliente : ")

    if nome in cadastroDeClientes:
        print("\n Informações do Cliente: ")
        print("Nome: ", nome)
        print("Genero: ", cadastroDeClientes[nome]['genero'])
        if "placa" in cadastroDeClientes[nome]:
            print(f"Placa do carro: {cadastroDeClientes[nome]['placa']}")
            print(f"Quilometragem contratada: {cadastroDeClientes[nome]['quilometragem']}")
            print(f"Dias contratados: {cadastroDeClientes[nome]['diasContrato']}")
            print(f"Valor da fatura: R${round(cadastroDeClientes[nome]['custoDeAluguel'], 3)}")
        else:
            print("Não possui carro alugado")

    else:
        print("\nCliente não encontrado.")

def ExcluirCliente():
    nome = input("Digite o nome do cliente a deletar: ")

    if nome in cadastroDeClientes:
        del cadastroDeClientes[nome]
        print("Cliente excluido")
    else:
        print("\nCliente não encontrado.")

def ListarCliente():
    if cadastroDeClientes:
        print("\nClientes Cadastrados: ")
        for cliente, info in cadastroDeClientes.items():
            print("\nNome: ", cliente)

    else:
        print("\nNão há clientes cadastrados.")

def AlugarCarro():
    nome = input("Digite o nome do cliente que irá alugar: ")

    quilometragemContradada = input("Informe quilometragem a contratar: ")
    while not ValidaNumero(quilometragemContradada):
        print("Por favor, insira um número válido para a quilometragem.")
        quilometragemContradada = input("Informe quilometragem a contratar: ")
    quilometragemContradada = int(quilometragemContradada)

    diasContratados = input("Informe quantos dias de contrato: ")
    while not ValidaNumero(diasContratados):
        print("Por favor, insira um número válido para os dias.")
        diasContratados = input("Informe quantos dias de contrato: ")
    diasContratados = int(diasContratados)
    custoDeAluguel = (quilometragemContradada * 0.1) + (diasContratados * 70)
    placaCarro = ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + "-" + ''.join(
        random.choice(string.digits) for _ in range(4))

    if nome in cadastroDeClientes:
        cadastroDeClientes[nome].update({"placa": placaCarro,
                                         "diasContrato": diasContratados,
                                         "quilometragem": quilometragemContradada,
                                         "custoDeAluguel": custoDeAluguel
                                         })
        print(f"\nAluguel realizado")
        print("Dados do aluguel: ")
        print(f"\n Nome do cliente: {nome}")
        print(f"Placa do carro: {placaCarro}")
        print(f"Quilometragem contratada: {quilometragemContradada}")
        print(f"Dias contratados: {diasContratados}")
        print(f"Valor da fatura: R${round(custoDeAluguel, 2)}")


    else:
        print("\nCliente não encontrado.")

def CalculaMediaDeAlugueis():
    totalDeAlugueis = 0
    totalDeClientesComAlugueis = 0

    for cliente, info in cadastroDeClientes.items():
        if "custoDeAluguel" in info:
            totalDeAlugueis += info["custoDeAluguel"]
            totalDeClientesComAlugueis += 1

    if totalDeClientesComAlugueis > 0:
        CalculaMediaDeAlugueis = totalDeAlugueis / totalDeClientesComAlugueis
        print(f"A média do custo de aluguel dos clientes é : R${round(CalculaMediaDeAlugueis, 2)}")

    else:
        print("Nenhum cliente com aluguel registrado.")

def CalculaValorTotalAlugueis():
    valorTotalDeAlugueis = 0

    for client, info in cadastroDeClientes.items():
        if "custoDeAluguel" in info:
            valorTotalDeAlugueis += info["custoDeAluguel"]

    if valorTotalDeAlugueis > 0:

        print(f"O total de alugueis em reais é : R${round(valorTotalDeAlugueis, 2)}")

    else:
        print("Nenhum cliente com aluguel registrado.")

def criar_cadastro():
    while True:
        print("\n-----Seja bem vindo a LocAutos. Nossa alegria é te atender com qualidade.----")
        print("\n1. Inserir cliente")
        print("2. Pesquisar cliente")
        print("3. Excluir cliente")
        print("4. Listar clientes")
        print("5. Alugar Carro")
        print("6. Média de custo de aluguel")
        print("7. Total em alugueis")
        print("8. Sair")

        opcaoSelecionada = input("\nEscolha a opção desejada: ")

        if opcaoSelecionada == "1":
            InserirCliente()

        elif opcaoSelecionada == "2":
            PesquisarCliente()

        elif opcaoSelecionada == "3":
            ExcluirCliente()

        elif opcaoSelecionada == "4":
            ListarCliente()

        elif opcaoSelecionada == "5":
            AlugarCarro()

        elif opcaoSelecionada == "6":
            CalculaMediaDeAlugueis()

        elif opcaoSelecionada == "7":
            CalculaValorTotalAlugueis()

        elif opcaoSelecionada == "8":
            break
        else:
            print("\nOpção não encontrada. Por favor selecione uma valida.")
# endregion

# region Iniciação do Programa
cadastroDeClientes = {}
criar_cadastro()
# endregion

