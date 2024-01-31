def conjunto_vertices(mat:list)->list:
    return mat[0]

def conjunto_arestas(mat:list)->list:
    A = []
    i:int = 1
    while(i < len(mat)):
        j = i-1
        while(j < len(mat[0])):
            if(mat[i][j] == 1):
                A.append(f"{mat[0][i-1],mat[0][j]}")
            j += 1
        i += 1
    return A

def verifica_subgrafo(mat1, mat2: list):
    condicao1:bool = False
    condicao2:bool = False
    
    vertices_G = conjunto_vertices(mat1)
    print("Vértices de G:", vertices_G)
    vertices_H = conjunto_vertices(mat2)
    print("Vértices de H:", vertices_H)
    arestas_G = conjunto_arestas(mat1)
    print("\nArestas de G:", arestas_G)
    arestas_H = conjunto_arestas(mat2)
    print("Arestas de H:", arestas_H)
    
    for i in range(len(vertices_H)):
        if(vertices_H[i] in vertices_G):
            condicao1 = True
    
    for i in range(len(arestas_H)):
        if(arestas_H[i] in arestas_G):
            condicao2 = True
    
    if(condicao1 and condicao2):
        print("SIM, H é subgrafo de G")
    else:
        print("H NÃO é subgrafo de G")
    
def main():
    
    matriz_G:list = [
                    ["A", "B", "C"],
                    [0, 1, 1], 
                    [1, 0, 1], 
                    [1, 1, 0]] 
    
    matriz_H:list = [
                    ["A", "C"],
                    [0, 1],
                    [1, 0]]
    
    '''matriz_G:list = []
    nro_vertices_G = int(input("Insira a quantidade de vértices da matriz do grafo G: "))
    
    for i in range(nro_vertices_G):
        linha = []
        for j in range(nro_vertices_G):
            elem = int(input(f"Insira o elemento {i+1}{j+1} da matriz do grafo G: "))
            linha.append(elem)
        matriz_G.append(linha)
        
    matriz_H:list = []
    nro_vertices_H = int(input("Insira a quantidade de vértices da matriz do grafo H: "))
    
    for i in range(nro_vertices_H):
        linha = []
        for j in range(nro_vertices_H):
            elem = int(input(f"Insira o elemento {i+1}{j+1} da matriz do grafo H: "))
            linha.append(elem)
        matriz_H.append(linha)'''
        
    verifica_subgrafo(matriz_G,matriz_H)

    
    