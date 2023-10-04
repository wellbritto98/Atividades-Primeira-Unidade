
from num2words import num2words
from datetime import date


def EscreveDataDeNascimento(dia, mes, ano):

    
    if mes == "1":
        mes_extenso = "Janeiro"
    elif mes == "2":
        mes_extenso = "Fevereiro"
    elif mes == "3":
        mes_extenso =  "Março"
    elif mes == "4":
        mes_extenso =  "Abril"
    elif mes == "5":
        mes_extenso =  "Maio"
    elif mes == "6":
        mes_extenso = "Junho"
    elif mes == "7":
        mes_extenso = "Julho"
    elif mes == "8":
        mes_extenso =  "Agosto"
    elif mes == "9":
        mes_extenso = "Setembro"
    elif mes == "10":
        mes_extenso = "Outubro"
    elif mes == "11":
        mes_extenso = "Novembro"
    elif mes == "12":
        mes_extenso = "Dezembro"     
            
    print("Você nasceu em: ", dia, "de", mes_extenso , "de", ano)
    print("Você tem: ", date.today().year - ano, "anos")
   

dia = int(input("Digite o dia do seu nascimento: "))
while dia < 1 or dia > 31:
    print("Dia inválido.")
    dia = int(input("Digite o dia do seu nascimento: "))
mes = input("Digite o mês do seu nascimento: ")


while mes != "1" and mes != "2" and mes != "3" and mes != "4" and mes != "5" and mes != "6" and mes != "7" and mes != "8" and mes != "9" and mes != "10" and mes != "11" and mes != "12":
    print("Mês inválido.")
    mes = input("Digite o mês do seu nascimento: ")        	
    


ano = int(input("Digite o ano do seu nascimento: "))
while ano < 1 or ano > date.today().year:
    print("Ano inválido.")
    ano = int(input("Digite o ano do seu nascimento: "))
EscreveDataDeNascimento(dia, mes, ano)
    
    
