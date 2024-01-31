def multiplica_matrizes(mat1, mat2)->list:
    resultado = []
    i:int = 0

    while(i < len(mat1)):
        resultado.append([0] * len(mat1))
        i += 1

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                resultado[i][j] += mat1[i][k] * mat2[k][j]

    return resultado

def numero_caminhos(mat:list, mat_original: list, ini:int, fim:int, tam:int):
    if (tam == 0):
        nro_caminhos = mat[ini][fim]
        return nro_caminhos
    else:
        tam -= 1
        nova_mat = multiplica_matrizes(mat_original, mat)
        return numero_caminhos(nova_mat, mat_original, ini, fim, tam)

def main():
    matriz = [[0, 0, 1, 0, 0, 0], 
              [0, 0, 1, 0, 0, 0], 
              [1, 1, 0, 1, 0, 0], 
              [0, 0, 1, 0, 1, 1], 
              [0, 0, 0, 1, 0, 1], 
              [0, 0, 0, 1, 1, 0]]
    
    origem = int(input("Insira o vértice de origem: "))
    destino = int(input("Insira o vértice de destino: "))
    tamanho = int(input("Insira o tamanho do caminho: "))

    print(f"Número de caminhos de tamanho {tamanho} entre os vértices {origem} e {destino}: ", numero_caminhos(matriz, matriz, origem-1, destino-1, tamanho-1))
