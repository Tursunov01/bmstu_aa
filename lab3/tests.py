import sort
from time import process_time

TIMES = 3



def test_time_to_sort_arr(key, f): 
    t1, t2, t3 = 0, 0, 0
    for i in range(1000, 11000, 1000):

        f.write("{0}  |".format(i))
        for j in range(TIMES):

            arr = sort.generateArr(i, key)
        
            start = process_time()
            sort.bubbleSort(arr)
            end = process_time()

            t1 += (end - start)

            arr = sort.generateArr(i, key)
        
            start = process_time()
            sort.insertSort(arr)
            end = process_time()

            t2 += (end - start)

            arr = sort.generateArr(i, key)
        
            start = process_time()
            sort.gnomeSort(arr)
            end = process_time()

            t3 += (end - start)
        f.write(" {0:<.15f}    | {1:<.15f}    | {2:<.15f}    |\n".format(t1/TIMES, t2/TIMES,
                                                             t3/TIMES))

print("Timing starts....")

f = open('Sorted.txt', 'w')
f.write("Size  | Bubble   | Insert  | Gnome   |\n")
test_time_to_sort_arr("Sorted", f)
f.close()

f = open('Reverse.txt', 'w')
f.write("Size  | Bubble   | Insert  | Gnome   |\n")
test_time_to_sort_arr("Reverse", f)
f.close()

f = open('Random.txt', 'w')
f.write("Size  | Bubble   | Insert  | Gnome   |\n")
test_time_to_sort_arr("Random", f)
f.close()

print("Timing ended")
