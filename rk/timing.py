from main import *
from time import process_time, time, time_ns, perf_counter
# import timeit

TIMES = 5


def test_time():
    names = ['Robert Rodriguez', 'James Huang', 'Judy Medina',
             'Nicholas Lawrence', 'Joseph Ramirez', 'Patrick Williams',
             'Alexis White', 'Bridget Farley', 'Timothy Erickson'] 
    with open('results.txt', 'w') as f:

        f.write("Size      | standart            | binary              \n")

        
        for size in range(1, 10):

            print('Размер {0}'.format(size))

            f.write("{0}      |".format(size*1000))

            t1, t2 = 0, 0
            data = read_file(str(size*1000) + '.csv')
            tmp = data
            tmp.sort()

            for _ in range(TIMES):    
                
                start = perf_counter()
                _ = full_iteration(data, names[size-1])
                stop = perf_counter()
                
                t1 += (stop - start)

                start = perf_counter()
                _ = bin_search(tmp, names[size-1])
                stop = perf_counter()

                t2 += (stop - start)


            f.write(" {0:<.15f}   | {1:<.15f}   \n".format(t1/(TIMES), t2/(TIMES)))

print("Timing starts....")
test_time()
print("Timing ended")