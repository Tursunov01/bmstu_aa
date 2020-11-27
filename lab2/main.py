from classicVinograd import *
from classicMul import *
from impVinograd import *


def printMatrix(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            print(a[i][j], end = " ")
        print("\n")

def main():
    A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    m1 = classicMul(A, B)
    m2 = winograd_multi(A, B)
    m3 = imprv_winograd_multi(A, B)
    print("Классический способ\n")
    printMatrix(m1)
    print("Алгоритм Винограда\n")
    printMatrix(m2)
    print("Улучшенный Классический способ\n")
    printMatrix(m3)
    

if __name__ == "__main__":
    main()