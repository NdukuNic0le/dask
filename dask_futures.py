from __future__ import annotations
import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from dask.distributed import Client

def multiply_by_two(inp: int | float) -> int | float:
    time.sleep(1)
    return inp * 2

# outputs = []
# start = time.time()
# for inp in range (10):
#     output = multiply_by_two(inp)
#     outputs.append(output)
# end = time.time()

# print (outputs)
# print(f"it took {end-start: 2f}s to execute the loop.")

# futures = []
# start = time.time()
# with ThreadPoolExecutor(max_workers=5) as executor:
#     for inp in range(10):
#         future = executor.submit(multiply_by_two, inp)
#         print(f"Is it still running?: {future.running()}")
#         futures.append(future)
#     outputs = [future.result() for future in futures]
# end = time.time()
# print (outputs)
# print (f"It took {end-start:.2f}s to execute the loop")

# futures = []
# start = time.time()
# with ProcessPoolExecutor(max_workers=5) as executor:
#     for inp in range(10):
#         future = executor.submit(multiply_by_two, inp)
#         print(f"Is it still running?: {future.running()}")
#         futures.append(future)
#     outputs = [future.result() for future in futures]
# end = time.time()
# print (outputs)
# print (f"It took {end-start:.2f}s to execute the loop")
# del futures

if __name__ == "__main__":
    client = Client()

    # futures = []
    # start = time.time()
    # for inp in range (10):
    #     future = client.submit(multiply_by_two, inp)
    #     futures.append(future)
    # outputs = [future.result() for future in futures]
    # end = time.time()
    # print (outputs)
    # print (f"It took {end-start:.2f}s to execute the loop")

    # start = time.time()
    # inputs = list(range(10))
    # futures = client.map(multiply_by_two, inputs)
    # outputs = client.gather(futures)
    # end = time.time()
    # print (outputs)
    # print (f"It took {end-start:.2f}s to execute the loop")

    # del futures

    start = time.time()
    inputs = list(range(10))
    remote_inputs = client.scatter(inputs)
    futures = client.map (multiply_by_two, remote_inputs)
    outputs = client.gather(futures)
    end = time.time()

    print(outputs)
    print(f"It took {end-start:.2f}s to execute the loop.")

    del remote_inputs
    del futures


