from time import sleep

class LaberintoRaton:

    def __init__(self, lab):
        self.lab = lab
        self.n = len(lab)

        self.solucion = [[0 for _ in range(self.n)]
                          for _ in range(self.n)]

        self.encontrado = False

        # Orden solicitado:
        # abajo, derecha, arriba, izquierda
        self.movimientos = [
            (1, 0),   # abajo
            (0, 1),   # derecha
            (-1, 0),  # arriba
            (0, -1)   # izquierda
        ]

    def imprimir_matriz(self, matriz):
        for fila in matriz:
            print(fila)
        print()

    def es_valido(self, fila, col, vidas, visitado):

        if fila < 0 or fila >= self.n:
            return False

        if col < 0 or col >= self.n:
            return False

        if visitado[fila][col]:
            return False

        if self.lab[fila][col] == 0:
            return False

        return vidas > 0

    def costo_celda(self, valor):

        if valor == 'I' or valor == 'F':
            return 0

        if valor == -1:
            return 1

        if valor == -2:
            return 2

        return 0

    def backtracking(self, fila, col, vidas, visitado):

        if not self.es_valido(fila, col, vidas, visitado):
            return False

        valor = self.lab[fila][col]

        vidas_restantes = vidas - self.costo_celda(valor)

        if vidas_restantes <= 0:
            return False

        visitado[fila][col] = True
        self.solucion[fila][col] = 1

        print(
            f"Posición ({fila},{col}) -> "
            f"Valor: {valor} -> "
            f"Vidas: {vidas_restantes}"
        )

        sleep(0.3)

        # Llegó a la meta (F)
        if valor == 'F':
            self.encontrado = True
            return True

        # Explorar en el orden solicitado
        for df, dc in self.movimientos:

            nueva_fila = fila + df
            nueva_col = col + dc

            if self.backtracking(
                    nueva_fila,
                    nueva_col,
                    vidas_restantes,
                    visitado):

                return True

        # Backtracking
        self.solucion[fila][col] = 0
        visitado[fila][col] = False

        print(f"Retrocede desde ({fila},{col})")

        return False

    def resolver(self):

        inicio_fila = self.n - 1
        inicio_col = 0

        visitado = [[False for _ in range(self.n)]
                    for _ in range(self.n)]

        exito = self.backtracking(
            inicio_fila,
            inicio_col,
            3,
            visitado
        )

        return exito

laberinto = [
    ['F', 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ['I', 1, -1, 1, 1, 1, 0, 1, 1]
]

raton = LaberintoRaton(laberinto)

print("\nLaberinto a recorrer:\n")
raton.imprimir_matriz(laberinto)

resultado = raton.resolver()

if resultado:

    print("\nSe encontró una matriz solución: \n")


    raton.imprimir_matriz(raton.solucion)

else:

    print("\nNo existe una matriz solución.\n")