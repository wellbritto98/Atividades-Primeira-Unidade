#escreva um programa em
#Python que realize o cadastro de questões objetivas para uma prova
#com suas respectivas respostas.
#Na sequência o programa deve solicitar as respostas para cada questão
#e imprimir o resultado (acertos e erros). O programa deve permitir que
#mais de uma pessoa informe as respostas, até que digite SAIR.

import os

questoes = {}
usuarios = {}

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_questao():
    limpar_terminal()

    enunciado = input('Informe o enunciado da questão: ')
    letra_a = input("Informe a letra A da questão: ")
    letra_b = input("Informe a Letra B da questão: ")
    letra_c = input("Informe a Letra C da questão: ")
    letra_d = input("Informe a Letra D da questão: ")

    gabarito = input("Infome o gabarito (a, b, c ou d): ")
    while gabarito not in ["a", "b", "c", "d"]:
        print("Informe um gabarito válido.")
        gabarito = input("Infome o gabarito (a, b, c ou d): ")

    questoes[enunciado] = {
        "enunciado": enunciado,
        "alternativas":{
            "letra_a": letra_a,
            "letra_b": letra_b,
            "letra_c": letra_c,
            "letra_d": letra_d},
        "gabarito":gabarito}

    print(questoes)

def responder_questoes():
    limpar_terminal()

    for nome, usuario in usuarios.items():
        print(f"\nAgora é a vez de: {usuario['nome']}")
        for pergunta, resposta in questoes.items():
            print("\n")
            print(f"Pergunta: {pergunta}")
            print("a - "+ resposta["alternativas"]["letra_a"])
            print("b - "+ resposta["alternativas"]["letra_b"])
            print("c - "+ resposta["alternativas"]["letra_c"])
            print("d - "+ resposta["alternativas"]["letra_d"])

            resposta_usuario = input("\nInforme a resposta (a, b, c ou d): ")
            while resposta_usuario not in ["a", "b", "c", "d"]:
                print("Informe uma resposta válida.")
                resposta_usuario = input("\nInforme a resposta (a, b, c ou d): ")

            if resposta_usuario == resposta["gabarito"]:
                print("Resposta correta")
                usuario['acertos'] += 1
            else:
                print("Resposta errada")
                print(f"Resposta correta : {resposta['gabarito']}")
                usuario['erros'] += 1

        print(f"{usuario['nome']} acertou {usuario['acertos']} questões e errou {usuario['erros']} questões.")
        usuario['acertos'] = 0
        usuario['erros'] = 0

def ListarQuestoes():
    limpar_terminal()
    for pergunta, resposta in questoes.items():
        print(pergunta)
    print("\n")
    print("Deseja sair ?")
    print("1 - Sim")
    print("2 - Não")
    opcao = input("Informe a opção: ")
    if opcao == "1":
        limpar_terminal()
    else:
        limpar_terminal()
        ListarQuestoes()        

def cadastrar_usuario():
    limpar_terminal()

    nome = input("Informe o nome: ")
    usuarios[nome] = {
        "nome": nome,
        "acertos": 0,
        "erros": 0
    }  

def IniciaPrograma():
    while True:
        limpar_terminal()

        print("\n1. Cadastrar questão")
        print("2. Responder questões")
        print("3. Listar questões")
        print("4. Cadastrar usuario")
        opcao_selecionada= input("\nInforma a opcao: ")

        if opcao_selecionada =="1":
            cadastrar_questao()
        elif opcao_selecionada == "2":
            responder_questoes()
        elif opcao_selecionada == "3":
            ListarQuestoes()   
        elif opcao_selecionada == "4":
            cadastrar_usuario()             
        else:
            break

IniciaPrograma()
