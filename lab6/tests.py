import asyncio
from main import *
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from itertools import product
import time

executor = ThreadPoolExecutor(max_workers=10)  # thread pool
loop = asyncio.get_event_loop()  # event loop


m = 5  # amount of ants and cities
Q = (MIN_DISTANCE * m, MAX_DISTANCE * m, MAX_DISTANCE * m // 2)  # coefficient of the alleged best way

p = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7)  # coefficient of evaporation
a = (1, 2, 3)  # coefficient of strengthen the sense of smell
b = (1, 2, 3)  # coefficient of strengthen of desire
e = (0, 1, 2, 3)  # amount of elite ants
good_answers = ([0, 4, 1, 3, 2], 26), ([3, 4, 0, 1, 2], 26), \
               ([2, 0, 4, 1, 3], 26), ([2, 3, 4, 1, 0], 26), \
               ([1, 4, 0, 2, 3], 26), ([0, 4, 3, 2, 1], 26)


TIMES = 5

best_time = None
best_set = None
best_q = None


def test_on_set(foo, params):
    global best_time, best_set, best_q
    s, d, t, q = params[0], params[1], params[2], params[3]
    st = time.process_time()
    res = best_way(m, s[0], d, t, s[1], s[2], s[3], q)
    en = time.process_time() - st
    if res in good_answers:
        if best_time is None or en < best_time:
            best_time = en
            best_set = s
            best_q = q


async def level_T(d, gen):
    await asyncio.gather(*[level_times(d, t, TIMES) for t in gen])


async def level_times(d, t, times):
    await asyncio.gather(*[level_Q(d, t, Q) for i in range(times)])


async def level_Q(d, t, Q):
    global best_time, best_set, best_q
    await asyncio.gather(*[level_set(d, t, q, e, a, b, p) for q in Q])
    try:
        print("{} &  {:.5f} & {} & {}".format(t, best_time, best_q, best_set))
        best_time = None
        best_set = None
        best_q = None
    except TypeError:
        print("OOOOPs")


async def level_set(d, t, q, e, a, b, p):
    await asyncio.gather(*[runner(s, d, t, q) for s in product(e, a, b, p)])


async def runner(s, d, t, q):
    param = (s, d, t, q)
    await loop.run_in_executor(executor, test_on_set, 1, param)


async def test(d):
    global best_time, best_set, best_q
    t_max = (100, 200, 300, 400, 500)  # the amount of "generations"
    await level_T(d, t_max)
  

if __name__ == "__main__":
    d_fix = np.array([[0,   6,   3,   7,   1],
             [6,   0,   8,  10,   6],
             [3,   8,   0,   6,   7],
             [7,  10,   6,   0,   5],
             [1,   6,   7,   5,   0]], dtype=float)

    print("Test matrix of distance: {}\n\n\n".format(d_fix))
    loop.run_until_complete(test(d_fix))