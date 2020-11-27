import random

def bubbleSort(arr):
    size = len(arr) 
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertSort(arr):
    size = len(arr)
    for i in range(size):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def gnomeSort(arr):
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1] 
            if i > 1:
                i -= 1
    return arr

def generateArr(n, key):
    arr = []
    if key == "Sorted":
        for i in range(n):
            arr.append(i)
    elif key == "Reverse":
        for i in range(n, 0, -1):
            arr.append(i)
    elif key == "Random":
        for i in range(n):
            num = random.randint(0, 100)
            arr.append(num)
    return arr


def main():
    n = int(input("Input size of array: "))
    if n < 0:
        print("Size of array can not be less than zero")
    elif n == 0:
        print("You input n = 0. That's why your array is empty")
    else:
        key = input("Input key of appended elements(Sorted, reversed, random)")
        t = input("Input a method which you like to sort(Bubble, Gnome, Insertation)")
        arr = generateArr(n, key)
        if t == "Bubble":
            print("Before ", arr)
            arr = bubbleSort(arr)
        elif t == "Insertation":
            print("Before ", arr)
            arr = insertSort(arr)
        else:
            print("Before ", arr)
            arr = gnomeSort(arr)
        print("Result: ", arr)

if __name__ == "__main__":
    main()

