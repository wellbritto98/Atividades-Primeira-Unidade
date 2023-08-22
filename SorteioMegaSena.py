import random




def sortear_numeros():
    
    numeros_sorteados = random.sample(range(1,61),6)
    
    print(sorted(numeros_sorteados, key=int))

sortear_numeros()    
    