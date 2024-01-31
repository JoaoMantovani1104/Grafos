def conjunto_vertices(numVertices:int)->list:
    V = []
    for i in range(1,numVertices + 1):
        V.append(i)
        
    return V

def conjunto_arestas(mat:list)->list:
    A = []
    i:int = 0
    while(i < len(mat)):
        j = i
        while(j < len(mat)):
            if(mat[i][j] == 1):
                A.append(f"{i+1},{j+1}")
            j += 1
        i += 1
    return A

def main():
    
    matriz:list = [[0, 1, 1], 
                   [1, 0, 1], 
                   [1, 1, 0]]
    nro_vertices = len(matriz)
    
    """matriz:list = []
    nro_vertices = int(input("Insira a quantidade de vértices do grafo: "))
    
    for i in range(nro_vertices):
        linha = []
        for j in range(nro_vertices):
            elem = int(input(f"Insira o elemento {i+1}{j+1} da matriz: "))
            linha.append(elem)
        matriz.append(linha)"""
        
    print("Conjunto dos vértices do grafo:", conjunto_vertices(nro_vertices))
    print("Conjunto das arestas do grafo:", conjunto_arestas(matriz))