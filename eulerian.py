def verifica_euleriano(mat:list) -> str:
    lista_graus:list = []
    grau_atual:int
    graus_impar:int = 0

    for i in range(len(mat)):
        grau_atual = 0
        for j in range(len(mat)):
            if(mat[i][j] == 1):
                grau_atual += 1

        lista_graus.append(grau_atual)

    k:int = 0
    while(k < len(lista_graus)):
        if (lista_graus[k] % 2 != 0):
            graus_impar += 1
        k += 1

    if (graus_impar == 0):
        return "SIM!"
    elif (graus_impar <= 2):
        return "NÃO, mas é Semieuleriano!"
    else:
        return "NÃO, nem Semieuleriano!"

def main():
    matriz = [[0, 1, 1], 
              [1, 0 ,1], 
              [1, 1, 0]]
    
    print("O grafo é Euleriano?", verifica_euleriano(matriz))


