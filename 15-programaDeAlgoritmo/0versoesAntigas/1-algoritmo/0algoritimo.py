from random import shuffle
from time import sleep

lista = list(range(1, 11))
shuffle(lista)
print(lista)
guardarNumero = 0
tempoParaPercorrer = .5

for c in range(len(lista)):
    for i in range(len(lista)):
        sleep(tempoParaPercorrer)
        print('\n'*20)
        print(lista)
        #print(i, len(lista))
        if i+1 == len(lista):
            continue
        else:
            if lista[i] > lista[i+1]:
                guardarNumero = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = guardarNumero
                
        for i in reversed(range(len(lista))):
            sleep(tempoParaPercorrer)
            print('\n'*20)
            print(lista)
            #print(i, len(lista))
            if i+1 == len(lista):
                continue
            else:
                if lista[i] > lista[i+1]:
                    guardarNumero = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = guardarNumero
        