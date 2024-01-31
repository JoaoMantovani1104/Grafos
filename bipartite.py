def verifica_bipartido(mat:list) -> bool:
    v1:list = []
    v2:list = []

    i:int = 0
    while(i < len(mat)):
        j = i
        while(j < len(mat)):
            if(mat[i][j] == 0):
                v1.append(j + 1)
            else:
                if(v2 == []):
                    v2.append(j + 1)
                else:
                    for k in range(len(v2)):
                        if(mat[v2[k] - 1][j] == 0):
                            v2.append(j + 1)
                        else:
                            return False
                        
            if(len(v1)+len(v2) == len(mat)):
                print("\nV1:", v1)
                print("V2:", v2)
                return True

            j += 1
        i += 1
    
    print("\nV1:", v1)
    print("V2:", v2)
    return True


def main():
    matriz = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

    print("Matriz informada:")
    for i in range(len(matriz)):
        print(matriz[i])

    if verifica_bipartido(matriz):
        print("\nO grafo é bipartido!")
    else:
        print("\nO grafo não é bipartido!")