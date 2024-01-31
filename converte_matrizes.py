def converte(mat:list):
    nro_vertices:int = len(mat[0])
    nova_matriz:list = []
    isIncidencia:bool = False
    
    for i in range(len(mat)):
        for j in range(nro_vertices):
            if mat[i][j] == -1:
                isIncidencia = True
                         
    if isIncidencia:
        lista_arestas = []
        indice1 = -1
        indice2 = -1
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] == 1):
                    indice1 = j
                elif(mat[i][j] == -1):
                    indice2 = j
                if(indice1 != -1) and (indice2 != -1):
                    lista_arestas.append([indice1,indice2])
                    lista_arestas.append([indice2,indice1])
                    indice1, indice2 = -1, -1
        for i in range(nro_vertices):
            linha = [0] * nro_vertices
            nova_matriz.append(linha)
            
        for i in range(len(lista_arestas)-1):
            indice = lista_arestas[i]
            nova_matriz[indice[0]][indice[1]] = 1

        print("\nMatriz convertida: ")
        k:int = 0
        while(k < len(nova_matriz)):
            print(nova_matriz[k])
            k += 1           
    else:
        i:int = 0
        while(i < nro_vertices):
            j = i
            while(j < nro_vertices):
                if(mat[i][j] == 1):
                    nova_linha1 = [0] * nro_vertices
                    nova_linha1[i] = 1
                    nova_linha1[j] = -1
                    nova_matriz.append(nova_linha1)
                    
                    nova_linha2 = [0] * nro_vertices
                    nova_linha2[i] = -1
                    nova_linha2[j] = 1
                    
                    nova_matriz.append(nova_linha2)
                j += 1
            i += 1
        
        print("\nMatriz convertida: ")
        k:int = len(nova_matriz) - 1
        while(k > -1):
            print(nova_matriz[k])
            k -= 1
        
def main():
    matriz_adjacencia = [[0, 1, 1], 
                         [1, 0, 1], 
                         [1, 1, 0]]
    matriz_incidencia = [[0, -1, 1], 
                         [0, 1, -1], 
                         [1, 0, -1], 
                         [-1, 0, 1], 
                         [1, -1, 0], 
                         [-1, 1, 0]]
    
    print("\nMatriz informada: ")
    for i in range(len(matriz_adjacencia)):
        print(matriz_adjacencia[i])
    
    converte(matriz_adjacencia)
                