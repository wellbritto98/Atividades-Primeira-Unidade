import random

def solicitar_aposta():
    numeros_escolhidos = []
    print("Por favor, escolha entre 15 a 18 números, sem repetição e entre 1 e 25.")

    quantidade_dezenas = 0
    while quantidade_dezenas < 15 or quantidade_dezenas > 18:
        quantidade_dezenas = int(input("Quantos números você quer marcar? (entre 15 e 18): "))

    for i in range(quantidade_dezenas):
        while True:
            numero = int(input(f"Informe o {i + 1}º número: "))
            if numero not in range(1, 26):
                print("Dezena inválida.")
            elif numero in numeros_escolhidos:
                print("Número repetido.")
            else:
                numeros_escolhidos.append(numero)
                break

    return sorted(numeros_escolhidos)

def surpresinha():
    return sorted(random.sample(range(1, 26), 18))

def sorteio_loteria():
    return sorted(random.sample(range(1, 26), 15))

def iniciar_sistema_loteria():
    print("\n-----LotoFacil, se divirta ganhando..----")

    # Solicitando aposta do usuário
    aposta_usuario = solicitar_aposta()


    # Gerando duas Surpresinhas
    surpresinha1 = surpresinha()
    surpresinha2 = surpresinha()
    resultado = sorteio_loteria()
    acerto_manual = len(set(resultado) & set(aposta_usuario) )
    acerto_surpresinha1 = len(set(resultado) & set(surpresinha1) )
    acerto_surpresinha2 = len(set(resultado) & set(surpresinha2))
    print(f"Sua aposta: {aposta_usuario}, total de {acerto_manual} acertos")
    print(f"Surpresinha 1: {surpresinha1}, total de {acerto_surpresinha1} acertos.")
    print(f"Surpresinha 2: {surpresinha2}, total de {acerto_surpresinha2} acertos.")

    # Simulando o resultado da Lotofácil

    print(f"Resultado do concurso da Lotofácil: {resultado}")

    print("Obrigado. Até mais!")

iniciar_sistema_loteria()