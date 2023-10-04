def area_triangulo(base, altura):
    return (base * altura) / 2

def area_retangulo(base, altura):
    return base * altura

def area_circulo(raio):
    return 3.14 * (raio ** 2)

while True:
    forma_geometrica = input("Escolha a forma geométrica: \n 1. triangulo\n 2. retangulo\n 3.circulo\n 0. Sair.\n")
    if forma_geometrica == "1":
        base = float(input("Informe a base do triangulo: "))
        altura = float(input("Informe a altura do triangulo: "))
        print(f"A area do triangulo é: {area_triangulo(base, altura)}")
    elif forma_geometrica == "2":
        base = float(input("Informe a base do retangulo: "))
        altura = float(input("Informe a altura do retangulo: "))
        print(f"A area do retangulo é: {area_retangulo(base, altura)}")
    elif forma_geometrica == "3":
        raio = float(input("Informe o raio do circulo: "))
        print(f"A area do circulo é: {area_circulo(raio)}")
    elif forma_geometrica == "0":
        break


            

