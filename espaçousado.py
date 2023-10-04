

pessoas = {}
armazenamento_total = 0

def cadastro():
    global armazenamento_total

    id = len(pessoas) + 1
    nome = input("Digite o nome: ")
    espaco_utilizado = float(input("Digite o espaço utilizado: ")) 

    armazenamento_total += espaco_utilizado

    pessoas[id] = {
        'nome': nome,
        'espaco_utilizado': round(espaco_utilizado,2),
        'porcentagem_do_uso': round((espaco_utilizado / armazenamento_total) * 100,2)
    }

    print(pessoas)

def atualizar_porcentagem_de_uso_das_pessoas():
    global armazenamento_total

    for id, pessoa in pessoas.items():
        pessoa['porcentagem_do_uso'] = round((pessoa['espaco_utilizado'] / armazenamento_total) * 100,2)

def cadastrar_arquivo_com_pessoas_em_ordem_id():
    with open("pessoas.txt", "a") as arquivo:
        for id, pessoa in sorted(pessoas.items()):
            arquivo.write(f"{id}         {pessoa['nome']}         {pessoa['espaco_utilizado']}         {pessoa['porcentagem_do_uso']}%\n")
        arquivo.write(f"\n\nEspaço Total: {armazenamento_total}")
        arquivo.write(f"\nMedia do armazenamento utilizado: {armazenamento_total / len(pessoas)}")  


while True:
    opcao = int(input("1 - Cadastrar\n2 - Cadastrar arquivo \n 3 - Sair\nDigite a opção: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        atualizar_porcentagem_de_uso_das_pessoas()
        cadastrar_arquivo_com_pessoas_em_ordem_id()
    else:
        break





    