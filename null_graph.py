def verifica_nulo (mat: list):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(mat[i][j] != 0):
                print("NÃO é nulo")
    print("SIM, é nulo")

def main():
    
    matriz:list = [[0, 0, 0], 
                   [0, 0, 0], 
                   [0, 0, 0]]
    nro_vertices = len(matriz)
    
    """matriz:list = []
    nro_vertices = int(input("Insira a quantidade de vértices do grafo: "))
    
    for i in range(nro_vertices):
        linha = []
        for j in range(nro_vertices):
            elem = int(input(f"Insira o elemento {i+1}{j+1} da matriz: "))
            linha.append(elem)
        matriz.append(linha)"""
        
    verifica_nulo(matriz)