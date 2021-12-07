import datetime
import psutil
import os

# buffer testing
def t1():
    available_memory_B = psutil.virtual_memory().available
    available_memory_GB = psutil.virtual_memory().available / 10**9
    # print('Available Memory: GByte = ', available_memory_GB, ' Byte =', available_memory_B)

    test_buffer = 2147483647
    print(test_buffer)

    # exit()

    print('Buffer: GByte =', (test_buffer / 10**9), ' Byte =', test_buffer)
    mem_threshold_B = 536870912 # 512 megabytes
    time_start = datetime.datetime.now()

    with open('../.input//A3_S1_LALL_R1_001(2).fasta', buffering=test_buffer) as file:
        pass

    time_end = datetime.datetime.now()  # end runtime record
    module_runtime = time_end - time_start
    print('- Runtime:', int(module_runtime.total_seconds() * 1000), 'ms')

# mem checker
def t2(debug, free_mem_percent):
    global buffer_size
    buffer_size = 0

    free_mem_per = free_mem_percent # % of free memory that program can used
    buffer_max = 2147483647 # max value for CInt ~2.15 GB

    free_mem = psutil.virtual_memory().available # available memory
    available_mem = round(free_mem * free_mem_per / 100) # memory available to program

    # check to not surpass free memory percent
    if available_mem >= buffer_max:
        buffer_size = buffer_max
    else:
        buffer_size = available_mem

    # debugging
    if debug is True:
        os.system('cls')
        print('[Buffer Information]')
        print('Available %:            ', free_mem_per,
              '\n\nFree Memory:\t        ', free_mem,
              '\nAvailable Memory:\t', available_mem,
              '\n\nBuffer Size:            ', buffer_size,
              '\nBuffer Max:             ', buffer_max,
              '\n')
        os.system('pause')

# inplace print test - Neat!
def t3():
    for i in range(300000000000000000000):
        print(i, end='\r')