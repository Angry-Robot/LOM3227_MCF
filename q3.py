import numpy.random as rd
import numpy as np
import math



def tempo_de_espera():
    pessoa=rd.randint(0,86400)/3600
    onibus=math.trunc(pessoa)
    x=rd.randint(0,3600)/3600
    onibus2=onibus + x
    
    if pessoa>onibus and pessoa<onibus2:
        t=(onibus2-pessoa)

    elif pessoa>onibus2 and pessoa<(onibus+1):
        t=((onibus+1)-pessoa)

    elif pessoa == onibus:
        t=0

    elif pessoa == onibus2:
        t=0

    tempo=t*60
    return tempo

def média():
    N = 100000
    amostra = 0 
  
    for n in range(N):
       
        amostra += (tempo_de_espera())
    
    print(amostra/N)
    
média()

# #abaixo código para testar as contas K vezes para conferir 
K=5
avg = 0
sum = 0
for k in range(K):
    print()
    print('Tentativa ',K)
    sum = média()
    sum += média()
avg = sum/k