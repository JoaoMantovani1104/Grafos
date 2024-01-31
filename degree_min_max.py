def calcula_graus(mat:list)->list:
    lista_graus = []
    for i in range(len(mat)):
        grau_parcial:int = 0
        for j in range(len(mat)):
            if (mat[i][j] == 1) or (mat[i][j] == -1):
                if(i == j):
                    grau_parcial += 2
                else:
                    grau_parcial += 1 
        lista_graus.append(grau_parcial)
    
    return lista_graus

def main():
    
    matriz:list = [[0, 1, 0], 
                   [-1, 1, 1], 
                   [0, -1, 0]]
    vertice = int(input(("Insira o número do vértice que deseja calcular o grau: ")))
    nro_vertices = len(matriz)
    
    """matriz:list = []
    nro_vertices = int(input("Insira a quantidade de vértices do grafo: "))
    
    for i in range(nro_vertices):
        linha = []
        for j in range(nro_vertices):
            elem = int(input(f"Insira o elemento {i+1}{j+1} da matriz: "))
            linha.append(elem)
        matriz.append(linha)"""
        
    
    lista_dos_graus = calcula_graus(matriz)
    
    print(f"Grau do vértice {vertice}:", lista_dos_graus[vertice-1])
    
    lista_dos_graus.sort()
    print("Grau mínimo:", lista_dos_graus[0])
    print("Grau máximo:", lista_dos_graus[nro_vertices-1])
    
    