import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def EscolherPalavra():
    global palavra
    palavra = input("Qual a palavra para acertar? ").lower().strip()
    limpar_terminal()
    print(f"\nPalavra escolhida. Dica: possui {len(palavra)} letras.")

def mostrar_progresso(palavra, letras_acertadas):
    progresso = ''
    for letra in palavra:
        if letra in letras_acertadas:
            progresso += letra + ' '
        else:
            progresso += '_ '
    return progresso

def IniciarJogo():
    limpar_terminal()
    letras_da_palavra = []
    tentativas = 0

    while tentativas < 3:
        print(mostrar_progresso(palavra, letras_da_palavra))
        
        letra = input("Escolha uma letra: ").lower().strip()
        
        if len(letra) != 1:
            print("Por favor, insira apenas uma letra.")
            continue
        
        if letra in letras_da_palavra:
            print("Você já escolheu essa letra.")
            continue
        
        if letra in palavra:
            print("Você acertou uma letra.")
            letras_da_palavra.append(letra)
            
            if set(letras_da_palavra) == set(palavra):
                print(f"\nParabéns! Você acertou. A palavra era '{palavra}'.")
                return
        else:
            tentativas += 1
            if tentativas < 3:
                print(f"Você errou. Você ainda tem {3 - tentativas} tentativas.")
            else:
                print(f"\nGame over! A palavra correta era: '{palavra}'.")

def IniciarMenuDoJogo():
    while True:
        limpar_terminal()

        print("\nSeja bem-vindo ao jogo da forca! Por favor, escolha uma opção:")
        print("\n1. Escolher nova palavra")
        print("2. Iniciar tentativas")
        print("3. Sair")

        opcao_selecionada = input("\nInforme uma opção: ")

        if opcao_selecionada == "1":
            EscolherPalavra()
        elif opcao_selecionada == "2":
            IniciarJogo()
        else:
            break

IniciarMenuDoJogo()
