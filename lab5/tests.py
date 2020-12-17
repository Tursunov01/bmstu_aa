from main import *

TIMES = 1
 
def test_traditional():
    start_time = time.time()
    start_clock = time.process_time()

    inpt = 10000000

    lvl_a = inpt, inpt * 2, inpt * 4
    
    logger.info("Running cpu-bound op on {}".format(lvl_a))
    lvl_b_0 = lvl_a[0], lvl_a[0] * 3, lvl_a[0] * 5
    logger.info("Running cpu-bound op on {}".format(lvl_b_0))
    lvl_b_1 = lvl_a[1], lvl_a[1] * 3, lvl_a[1] * 5
    logger.info("Running cpu-bound op on {}".format(lvl_b_1))
    lvl_b_2 = lvl_a[2], lvl_a[2] * 3, lvl_a[2] * 5
    logger.info("Running cpu-bound op on {}".format(lvl_b_2))
    
    lvl_c = lvl_b_0
    
    branch_0 = sum(lvl_c)
    
    lvl_c = lvl_b_1
    
    branch_1 = sum(lvl_c)
    
    lvl_c = lvl_b_2
    
    branch_2 = sum(lvl_c)
    
    time.sleep(3 + 2 * 3 + 1 * 9)
    
    result = sum((branch_0, branch_1, branch_2))
    logger.info("Running cpu-bound op on ({}, {}, {})".format(branch_0, branch_1, branch_2))
    
    logger.info("Completed ({}) in {} seconds and {} cpu-time".format(result, time.time() - start_time, time.process_time() - start_clock))


def testing_threads(fName):
    threads = [ 1,2,4,8,9,16,32,64 ]
    print('...TIMING...\n\n')

    with open(fName, 'w') as f:

        f.write("threads      |      Time     |     CPU Time    \n")

        for i in threads:

            print('Thread {0}'.format(i))

            f.write("{0}|".format(i))
            t1 = 0
            t2 = 0
            
            for j in range(TIMES):    
                executor = ThreadPoolExecutor(max_workers=i)
                start_work_time = time.time()
                start_process_clock = time.process_time()
                result = loop.run_until_complete(process_pipeline(2))

                t1 += (time.time() - start_work_time)
                t2 += (time.process_time() - start_process_clock)

            f.write(" {0:<.15f}   | {1:<.15f}   \n".format(t1/TIMES, t2/TIMES))

    print('...end...\n\n')


if __name__ == "__main__":
    # test_traditional()
    testing_threads("results.txt")