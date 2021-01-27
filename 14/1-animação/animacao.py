from time import sleep
from random import shuffle
from os import system

f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

# definição do tamanho da lista
tamanhoDaLista = 10
lista = list(range(1, tamanhoDaLista))

shuffle(lista)


print()

# mostrar lista, serve para mostrar a lista de forma legal
def Mostrar(mostrarLista):
    #system('clear')
    for cs in mostrarLista:
        for c in cs:
            if c > 0:
                print(f'{c}', end='')
            else:
                print(' ', end='')
        print()
    
    sleep(.04)                  
    #mostrarLista.clear()

    
    
#mostrarLista[1][1] = 1

# aqui serve para tranformar uma lista em matrix para mostrar() conseguir mostrar
def converterPMostrar(n):
    
    mostrarLista = [([0 for i in range(tamanhoDaLista)]) for i in range(tamanhoDaLista)]
    for contador in range(len(lista)):
        
        for i, chars in enumerate(mostrarLista[::-1]):
            if lista[contador] == i: break        

            chars[contador] = 1
            if contador == n:
                chars[contador] = 2    
    
    Mostrar(mostrarLista)
    mostrarLista.clear()
    sleep(.02)



converterPMostrar(3)