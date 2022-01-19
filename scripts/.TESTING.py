import datetime
import sys
import time
from threading import Thread
from multiprocessing import Process
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

# fna_formatter algorithm
def t4():
    os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')

    # bp = single letter code
    #   - remove all headers
    #   - format sequences so they are around 200bps
    #   - create a partitioning algorithm that allows the use
    #     of large files when sufficient RAM is not available
    #       > could use char count to estimate amount of RAM to use;

    # TODO: make pathing dynamic
    PATH = '../.input/A3_S1_LALL_R1_001(2).fasta'
    output_file_name = '../.output/A3_S1_LALL_R1_001(2)_formatted.fasta'
    sample_file = '../.output/A3_S1_LALL_R1_001(2)_sample.fasta'
    running = False

    with open(PATH) as file:
        process = psutil.Process()

        enable_debug = True
        create_sample = True  # kill alg after first purge, creates sample for presentation

        def debug():
            stat_msg = {0 : ''}

        def format_alg():
            print('Starting Algorithm...')

            data_size = 50

            line_data = []
            char_data = []
            index = 4   #200

            for line in file:
                if line[0] == '>':
                    line = ''

                if len(line_data) >= data_size:

                    while index < len(char_data):
                        char_data.insert(index, '\n')
                        index += index

                    print(char_data)
                    exit()

                line = ''.join(line).replace('\n', '')
                # char_data = [char ]


        format_alg()

# t4()

