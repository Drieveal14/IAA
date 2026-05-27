import random
import time
def crear_matriz(n: int):
    """Crea una matriz nxn con enteros aleatorios desde el 0 hasta el 99."""
    return [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]

def multiplicar(A, B):
    m = len(A)
    n1 = len(A[0])
    n2 = len(B)
    p = len(B[0])

    if n1 != n2:
        raise Exception("Las matrices no se pueden multiplicar")

    # Transpuesta de B: si B es n2 x p, B_T será p x n2
    B_T = [[0 for _ in range(n2)] for _ in range(p)]

    for i in range(n2):
        filaB = B[i]
        for j in range(p):
            B_T[j][i] = filaB[j]

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        filaA = A[i]
        for j in range(p):
            columnaB = B_T[j]
            s = 0
            for k in range(n1):
                s += filaA[k] * columnaB[k]
            result[i][j] = s

    return result

def imprimir_matriz(M):
    for fila in M:
        print(fila)


def multiplicacion(n: int):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo")

    print(f"\nCreando matrices {n}x{n} con valores aleatorios 0..99...")
    A = crear_matriz(n)
    B = crear_matriz(n)

    print("Imprimiendo matriz A")
    imprimir_matriz(A)
    print("Imprimiendo matriz B")
    imprimir_matriz(B)


    print("\nMultiplicando matriz completa")
    t2 = time.time()
    C = multiplicar(A, B)
    t3 = time.time()
    print(f"Tiempo multiplicación completa: {t3 - t2:.4f} s")

    imprimir_matriz(C)
   



if __name__ == "__main__":
    #Caso completo: O(n³)
    try:
        n = int(input("Ingrese el tamaño n de la matriz (matriz cuadrada): "))
        multiplicacion(n)
    except ValueError as e:
        print(f"Error: {e}")
