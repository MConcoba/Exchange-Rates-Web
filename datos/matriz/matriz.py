"""
MATRIZ 5X5
                Columnas
           0  1  2  3  4  5
        0| 1  2  3  4  5  6  |
        1| 8  1  2  3  6  2  |
Filas   2| 2  4  2  3  6  4  |
        3| 1  6  9  0  3  2  |
        4| 5  7  8  3  4  9  |

"""
matriz = [[1,2,3,4,5,6], [8,1,2,3,6,2], [2,4,2,3,6,4], [1,6,9,0,3,2], [5,7,8,3,4,9]]




matriz2 = []

filas = 5
columas = 6

for x in range(filas):
    matriz2.append([])
    for y in range(columas):
        matriz2[x].append(y)

""" for m in matriz2:
    print(m) """

matriz3 = [list(range(10)) for x in range(10)]

for x in matriz3:
    print(x)