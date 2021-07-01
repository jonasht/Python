from posix import ST_NOATIME
from uteis import *
import colors as c



matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

def find(lista, oque):
    oque = str(oque)
    lista = map(str, lista)
    
    for i, char in enumerate(lista):
        if char == oque:
            return i
            
def colocarNumeros(matriz):
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):

            if m == 'X':
                matriz[i][ii] = 3
            elif m == 'O':
                matriz[i][ii] = 2
            else:
                matriz[i][ii] = 0
    return matriz
                
def somarNumeros(matriz):
    matriz = colocarNumeros(matriz)
    numeros = []
    soma = 0

    soma = 0
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):
            soma += matriz[ii][i]
        numeros.append(soma)
            
        soma = 0
    
    soma = 0
    
    # /
    for i in range(3):
            soma += matriz[2-i][i]

    # soma todas as fileiras
    numeros.append(soma)
    for ms in matriz:
        numeros.append(sum(ms))

    soma=0
    # \
    for i in range(3):
        soma += matriz[i][i]
    
    numeros.append(soma)
    # print(numeros)
    return numeros

def fazerJogada(matriz):
    numeros = somarNumeros(matriz)
    print(numeros)
    
mostrar(matriz)
colocar('O', 0, 0, matriz)
colocar('X', 0, 1, matriz)
colocar('O', 2, 2, matriz)
colocar('X', 1, 1, matriz)
colocar('O', 2, 0, matriz)



mostrar(matriz)
# somarNumeros(matriz)
print(fazerJogada(matriz))



        

        
