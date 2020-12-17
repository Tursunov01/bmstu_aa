import asyncio
import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(format="[%(thread)-5d]%(asctime)s: %(message)s")
logger = logging.getLogger('async')
logger.setLevel(logging.INFO)

executor = ThreadPoolExecutor(max_workers=9)  # thread pool
loop = asyncio.get_event_loop()  # event loop


def cpu_bound_op(exec_time, *data):   # fake long-running func
    # logger.info("Running cpu-bound op on {} for {} seconds".format(data, exec_time))
    time.sleep(exec_time)
    return sum(data)


async def process_pipeline(data):
    # just pass the data along to level_a and return the results
    results = await level_a(data)  # Waiting for the level a
    return results


async def level_a(data):
    level_b_inputs = data, 2 * data, 4 * data
    results = await asyncio.gather(*[level_b(val) for val in level_b_inputs])  # aggregate results from the level b
    # print("AAAA ", results)
    result = await loop.run_in_executor(executor, cpu_bound_op, 3, *results)
    # print("AAAA1 ", result)
    return result


async def level_b(data):
    # similar to level a
    level_c_inputs = data, 3 * data, 5 * data
    results = await asyncio.gather(*[level_c(val) for val in level_c_inputs])
    # print("BBBB ", results)
    result = await loop.run_in_executor(executor, cpu_bound_op, 2, *results)
    # print("BBBB1 ", result)
    return result


async def level_c(data):
    result = await loop.run_in_executor(executor, cpu_bound_op, 1, data)
    return result


def main():
    start_work_time = time.time()
    start_process_clock = time.process_time()
    result = loop.run_until_complete(process_pipeline(10000000))
    # print(result)
    # logger.info("Completed ({}) in {} seconds and {} cpu-time".format(result, time.time() - start_work_time, time.process_time() - start_process_clock))


if __name__ == '__main__':
    main()