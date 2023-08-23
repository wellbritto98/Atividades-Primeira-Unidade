#Faça um programa que usa a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programador deverá solicitar ao usuario o valor da prestação e o numero de dias em atraso e passar estes valores para a função valorPagamento,
#que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
#O programa deverá então exibir o valor a ser pago na tela.
#Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
#Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
#O cálculo do valor a ser pago é feito da seguinte forma.
#Para pagamentos sem atraso, cobrar o valor da prestação.

#Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

relatorio_do_dia = {"quantidade":0, "valor":0}
def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = (valor * 0.001) * dias
        relatorio_do_dia["quantidade"] += 1
        relatorio_do_dia["valor"] += valor + multa + juros
        return valor + multa + juros

valor=1 #não pode ser 0, pois o programa não entra no while, mesmo sendo 1, a variavel será alterada no while
while valor!= 0:
    valor = float(input("Digite o valor da prestação: "))
    dias = int(input("Digite o numero de dias em atraso: "))
    print("O valor a ser pago é: ", valorPagamento(valor, dias))
    
if valor == 0:
    print("\nO relatório do dia é:\n ")
    print("Quantidade de prestações pagas: ", relatorio_do_dia["quantidade"])
    print("Valor total de prestações pagas: ", relatorio_do_dia["valor"])
        
    
        
