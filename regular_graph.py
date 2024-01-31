def verifica_regularidade(mat:list):
    lista_graus = []
    for i in range(len(mat)):
        grau_parcial = 0
        for j in range(len(mat)):
            if(mat[i][j] == 1):
                if(i == j):
                    print("NÃO é regular")
                else:
                    grau_parcial += 1
        lista_graus.append(grau_parcial)
        
    k:int = 0    
    while(k < len(lista_graus)-1):
        if(lista_graus[k] != lista_graus[k+1]):
            print("NÃO é regular")
        k += 1
    
    print(f"SIM, é um grafo {lista_graus[0]}-regular")

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
        
    verifica_regularidade(matriz)