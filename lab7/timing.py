from main import *
from time import process_time, time, time_ns

TIMES = 3

def generate():
    for i in range(1000, 11000, 1000):
        generate_data(i, str(i) + '.csv')

def test_time():
    names = ['robertpugh@sanchez.com', 'neaton@hotmail.com', 'veronicafisher@gmail.com',
             'lpatterson@yahoo.com', 'qdavis@davis.com', 'seanwood@black.com',
             'gthomas@hotmail.com', 'cody31@harris.com', 'bauermark@hotmail.com', 'cbailey@hotmail.com'] 
    with open('results.txt', 'w') as f:

        f.write("Size  | standart            | binary              | combined  \n")

        
        for size in range(1, 6):

            print('Размер {0}'.format(size))

            f.write("{0}      |".format(size*1000))

            t1, t2, t3 = 0, 0, 0

            for j in range(TIMES):    
                emails = read_csv(str(size*1000) + '.csv')

                start = process_time()
                result = full_iteration(emails, names[size])
                stop = process_time()

                t1 += (stop - start)

                start = process_time()
                result = bin_search(emails, names[size])
                stop = process_time()

                t2 += (stop - start)

                start = process_time()
                result = combined(emails, names[size])
                stop += process_time()

                t3 += (stop - start)

            f.write(" {0:<.15f}   | {1:<.15f}   | {2:<.15f} \n".format(t1/(TIMES), t2/(TIMES),
                                                             t3/(TIMES)))

print("Timing starts....")
test_time()
print("Timing ended")