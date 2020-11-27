from random import randint
from time import process_time
from main import *

TIMES = 10

def time_testing_size(fName):
    print('...TIMING...\n\n')

    with open(fName, 'w') as f:

        f.write("Size      |      Async Mul     |    Classic Mul     \n")

        for size in range(100, 1100, 100):

            print('Multiplication of matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = random_matrix(size, size)
            b = random_matrix(size, size)

            t1, t2 = 0, 0


            start = process_time()
            result = loop.run_until_complete(multi_async(a, b))
            stop = process_time()

            t1 += (stop - start)

            start = process_time()
            result_classic = multi(a, b)
            stop = process_time()

            t2 += (stop - start)

            f.write(" {0:<.15f}   | {1:<.15f}   \n".format(t1, t2))

        for size in range(101, 1101, 100):

            print('Multiplication of matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = random_matrix(size, size)
            b = random_matrix(size, size)

            t1, t2 = 0, 0

            start = process_time()
            result = loop.run_until_complete(multi_async(a, b))
            stop = process_time()

            t1 += (stop - start)

            start = process_time()
            result_classic = multi(a, b)
            stop = process_time()

            t2 += (stop - start)

            f.write(" {0:<.15f}   | {1:<.15f}   \n".format(t1, t2))

    print('...end...\n\n')

def testing_threads(fName):
    threads = [ 1,2,4,8,16,32,64 ]
    print('...TIMING...\n\n')
    a = random_matrix(400, 400)
    b = random_matrix(400, 400)

    with open(fName, 'w') as f:

        f.write("threads      |      Async Mul     \n")

        for i in threads:

            print('Thread {0}'.format(i))

            f.write("{0}|".format(i))
            t1 = 0
            
            for j in range(TIMES):    
                executor = ThreadPoolExecutor(max_workers=i)
                start = process_time()
                result = loop.run_until_complete(multi_async(a, b))
                stop = process_time()

                t1 += (stop - start)


            f.write(" {0:<.15f}\n".format(t1/TIMES))

    print('...end...\n\n')


if __name__ == '__main__':
    # time_testing_size("test40.txt")
    testing_threads("test_threads1.txt")