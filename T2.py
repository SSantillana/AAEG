import random

def crear_matriz(n):
    return [[random.randint(99, 999) for _ in range(n)] for _ in range(n)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{num:4}" for num in fila))

def contar_multiplos(matriz, fila_inicio, fila_fin, col_inicio, col_fin):

    if fila_inicio > fila_fin or col_inicio > col_fin:
        return 0
        
    if fila_inicio == fila_fin and col_inicio == col_fin:
        elemento = matriz[fila_inicio][col_inicio]
        if elemento % 5 == 0 or elemento % 7 == 0:
            return 1
        return 0

    fila_mitad = (fila_inicio + fila_fin) // 2
    col_mitad = (col_inicio + col_fin) // 2

    superior_izq = contar_multiplos(matriz, fila_inicio, fila_mitad, col_inicio, col_mitad)
    superior_der = contar_multiplos(matriz, fila_inicio, fila_mitad, col_mitad + 1, col_fin)
    inferior_izq = contar_multiplos(matriz, fila_mitad + 1, fila_fin, col_inicio, col_mitad)
    inferior_der = contar_multiplos(matriz, fila_mitad + 1, fila_fin, col_mitad + 1, col_fin)

    return superior_izq + superior_der + inferior_izq + inferior_der

def main():
    try:
        n = int(input("Ingrese tamaño N de la matriz (N x N): "))
        if n <= 0:
            print("Por favor, ingrese un número entero mayor a 0.")
            return
        matriz = crear_matriz(n)

        print("\nMatriz generada:")
        imprimir_matriz(matriz)
        
        print(f"\nNúmeros que son múltiplos de 5 o 7: ",contar_multiplos(matriz, 0, n - 1, 0, n - 1))
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()