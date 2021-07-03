# from ia import *
import colors as c
from uteis import *



# encontrar numero, mas deve ser substituido pela funcao index()
def find(lista, oque):
    oque = str(oque)
    lista = map(str, lista)
    
    for i, char in enumerate(lista):
        if char == oque:
            return i
            
# colocar numero no local de matriz
def colocarNumeros(matriz):
    matrizNum = [[0 for _ in range(3)] for _ in range(3)]

    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):

            if m == 'X':
                matrizNum[i][ii] = 3
            elif m == 'O':
                matrizNum[i][ii] = 2
            else:
                matrizNum[i][ii] = 0
    print('colocarNumero, matrizNum:', matrizNum)
    return matrizNum

# somar numeros, de todas possibidades  
def somarNumeros(matrizNum):
    matrizNum = colocarNumeros(matrizNum)
    numeros = []
    soma = 0
    
    for i, ms in enumerate(matrizNum):
        for ii, m in enumerate(ms):
            soma += matrizNum[ii][i]
        numeros.append(soma)
            
        soma = 0
    
    soma = 0
    
    # /
    for i in range(3):
            soma += matrizNum[2-i][i]

    # soma todas as fileiras
    numeros.append(soma)
    for ms in matrizNum:
        numeros.append(sum(ms))

    soma=0
    # \
    for i in range(3):
        soma += matrizNum[i][i]
    
    numeros.append(soma)
    
    print('somar numeros: numeros:', numeros)
    return numeros, matrizNum

# encontrar espaca na matrizNum para poder colocar em uma determinada fileira
def encontrarEspoco(opcao, matrizNum):
    fileira = []

    for i, ms in enumerate(matrizNum):
        if opcao == 1:
            if matrizNum[i][1]== 0:
                fileira.append([i, 1])

    print('fileira:', fileira)
    return fileira


def fazerJogada(matriz):
    numeros, matrizNum = somarNumeros(matriz)
    maior = 0
    
    for char in numeros:
        if char > maior and char <= 6:
            maior = char
    
    fileira = find(numeros, maior)
    
    print('retornarEspaço: fileira:', fileira, matrizNum)
    return encontrarEspoco(fileira, matrizNum)
    

# fazer a matriz
matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]


mostrar(matriz)
colocar('O', 0, 0, matriz)
colocar('X', 0, 1, matriz)
colocar('O', 2, 2, matriz)
colocar('X', 1, 1, matriz)
colocar('O', 2, 0, matriz)



mostrar(matriz)

jogada = fazerJogada(matriz)

print('jogada:', jogada)
colocar('X', jogada[0][0], jogada[0][1], matriz)
mostrar(matriz)


        

        
