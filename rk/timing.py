from exp import *
from main import *
from time import process_time, time, time_ns, perf_counter
# import timeit




def test_time():
    
    t1 = perf_counter()
    _ = polska("62+3*4-37+/")
    t2 = perf_counter()
    print(t2-t1)

print("Timing starts....")
test_time()
print("Timing ended")