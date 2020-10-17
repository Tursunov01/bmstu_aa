import random
import string
from time import time

def PrintMatrix(table, str1, str2):
    print("\n   ", end = " ")
    for i in str2:
        print(i, end = " ")

    for i in range(len(table)):
        if i:
            print("\n" + str1[i-1], end = " ")
        else:
            print("\n ", end = " ")
        for j in range(len(table[i])):
            print(table[i][j], end = " ")
    print("\n")


def LevTable(a, b):
    f = [[i+j if i*j == 0 else 0 for j in range(len(b) + 1)] for i in range (len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range (1, len(b) + 1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[len(a)][len(b)]

def LevRecursion(a, b):
    if a ==  "" or b == "": 
        return abs(len(a) - len(b))
    coef = 0 if (a[-1] == b[-1]) else 1
    return min(LevRecursion(a, b[:-1]) + 1,
               LevRecursion(a[:-1], b) + 1,
               LevRecursion(a[:-1], b[:-1]) + coef)

def DamLevRecursion(a, b):
    if a ==  "" or b == "":
        return abs(len(a) - len(b))
    coef = 0 if (a[-1] == b[-1]) else 1
    res = min(DamLevRecursion(a, b[:-1]) + 1,
              DamLevRecursion(a[:-1], b) + 1,
              DamLevRecursion(a[:-1], b[:-1]) + coef)
    if (len(a) >= 2 and len(b) >= 2 and a[-1] == b[-2] and a[-2] == b[-1]):
        res = min(res, DamLevRecursion(a[:-2], b[:-2]) + 1)
    return res 

def DamLevTable(a, b):
    f = [[i+j if i*j == 0 else 0 for j in range(len(b) + 1)] for i in range (len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
            if (i > 1 and j > 1) and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                f[i][j] = min(f[i][j], f[i-2][j-2] + 1)
    return f[len(a)][len(b)]

def GenerateString(strLength = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))

def GenMethod(method):
    str1 = input("Input str1: ")
    str2 = input("Input str2: ")
    res = method(str1, str2)
    print("Distance == ", res)


def TimeAnalysis(function, nIter, strLen = 5):
    t1 = time()
    for i in range(nIter):
        str1 = GenerateString(strLen)
        str2 = GenerateString(strLen)
        function(str1, str2)
    t2 = time()
    return (t2 - t1) / nIter


def Menu():
    flag = True
    print("Menu:\n \
\t1. Levenshtein recursion\n \
\t2. Levenshtein table\n \
\t3. Damerau–Levenshtein recursion\n \
\t4. Damerau–Levenshtein table\n \
\t5. Non recursion time analysis\n \
\t6. Recursion time analysis\n ")
    while(flag):
        choice = input("Make your choice: ")
        if (choice == "1"):
            GenMethod(LevRecursion)
        elif (choice == "2"):
            GenMethod(LevTable)
        elif (choice == "3"):
            GenMethod(DamLevRecursion)
        elif (choice == "4"):
            GenMethod(DamLevTable)
        elif (choice == "5"):
            n = 100
            for i in range(1, 1000, 50):
                print("Strlen: ", i)
                print("   Lev table       : ", "{0:.15f}".format(TimeAnalysis(LevTable, n, i)))
                print("   DamLev table    : ", "{0:.15f}".format(TimeAnalysis(DamLevTable, n, i)))
        elif (choice == "6"):
            n = 20
            for i in range(1, 11, 1):
                print("Strlen: ", i)
                print("   Lev recursion   : ", "{0:.15f}".format(TimeAnalysis(LevRecursion, n, i)))
                print("   DamLev recursion: ", "{0:.15f}".format(TimeAnalysis(DamLevRecursion, n, i)))
        else:
            flag = False
            
            
if __name__ == "__main__": 
    Menu()