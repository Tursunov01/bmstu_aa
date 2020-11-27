from random import randint
from time import process_time
from classicMul import classicMul
from classicVinograd import winograd_multi
from impVinograd import imprv_winograd_multi


TIMES = 3


def random_matrix(n, m):
    return [[randint(0, 100) for i in range(m)] for j in range(n)]


def time_testing():
    print('...TIMING...\n\n')

    with open('log1.txt', 'w') as f:

        f.write("Size      | Classic   | Winorgad  | Imprv Wino   | Impv Classic\n")

        for size in range(100, 400, 100):

            print('Multiplication of matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = random_matrix(size, size)
            b = random_matrix(size, size)

            t1, t2, t3 = 0, 0, 0

            for i in range(TIMES):

                start = process_time()
                res_class = classicMul(a, b)
                stop = process_time()
                print("Classic: ", stop- start)

                t1 += (stop - start)

                start = process_time()
                res_wino = winograd_multi(a, b)
                stop = process_time()
                print("Winograd: ", stop-start)

                t2 += (stop - start)

                start = process_time()
                res_wino_imprv = imprv_winograd_multi(a, b)
                stop = process_time()
                print("Improved Winograd: ", stop-start)

                t3 += (stop - start)

            f.write(" {0:<.15f}   | {1:<.15f}   | {2:<.15f} \n".format(t1/TIMES, t2/TIMES,
                                                             t3/TIMES))

        for size in range(101, 401, 100):
                size += 1

                print('Multiplication of matrix {0} X {0} '.format(size))

                f.write("{0} X {0} |".format(size))

                a = random_matrix(size, size)
                b = random_matrix(size, size)

                t1, t2, t3 = 0, 0, 0

                for i in range(TIMES):
                    start = process_time()
                    res_class = classicMul(a, b)
                    stop = process_time()
                    print("Classic: ", stop- start)

                    t1 += (stop - start)

                    start = process_time()
                    res_wino = winograd_multi(a, b)
                    stop = process_time()
                    print("Winograd: ", stop-start)

                    t2 += (stop - start)

                    start = process_time()
                    res_wino_imprv = imprv_winograd_multi(a, b)
                    stop = process_time()
                    print("Improved Winograd: ", stop-start)

                    t3 += (stop - start)

                f.write(" {0:<.5f}   | {1:<.5f}   | {2:<.5f}   \n".format(t1/ TIMES, t2/ TIMES,
                                                                                        t3/ TIMES))

    print('...end...\n\n')


if __name__ == '__main__':
    time_testing()