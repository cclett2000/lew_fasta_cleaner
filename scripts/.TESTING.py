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
    PATH = '../scripts/.test_data.test'
    output_file_name = '../.output/A3_S1_LALL_R1_001(2)_formatted.fasta'

    with open(PATH) as file:
        process = psutil.Process()

        enable_debug = True
        create_sample = False  # kill alg after first purge, creates sample for presentation

        # set partition size
        def set_list_size():
            list_size = 10**6  # set size of lists (default = 10**6 or 1 million lines)

            # list size check, sets list_size to file length if lower than set value
            print('>>> Getting File Line Count...')
            global size_check
            size_check = sum(1 for line in open(PATH))
            og_size = list_size

            if size_check <= list_size:
                list_size = size_check
                print('\t- Line Threshold Changed\n', '\t\tOld:', og_size, 'New:', list_size)
            print('Done.')

            return list_size

        # algorithm
        def format_alg():
            pass_count = 0          # keep track of number of passes through file
            list_size = set_list_size()
            remaining_lines = size_check

            line_list = []
            char_list = []
            index = 0             # index to place newline
            inc_index = 200       # incrementer

            print('\n>>> Starting Algorithm...')
            for line in file:
                # remove header
                if line[0] == '>':
                    line = ''

                # start work on data chunk (stop filling mem)
                if len(line_list) >= list_size - 1:
                    line_list_len = len(line_list)

                    # keep track of remaining lines
                    remaining_lines -= line_list_len

                    char_list = list(''.join(line_list))    # convert lines to char
                    line_list.clear()                       # clear line list

                    if enable_debug:
                        pass_count += 1
                        print('\t- Pass', pass_count)
                        print('\t\tchar_list size:', len(char_list))        # show char_list size
                        print('\t\tline_list size:', line_list_len)         # show line_list size

                    # insert newline in desired position
                    while index < len(char_list):
                        char_list.insert(index, '\n')
                        index += inc_index

                    char_list.append('\n')

                    if enable_debug:
                        print('\n\t\tNewline Insertion Done.')

                    write_file = open(output_file_name, 'a')
                    write_file.write(''.join(char_list))
                    write_file.close()

                    # write to file
                    if enable_debug:
                        print('\t\tSaved to File.')
                        print('\t\tRemaining Lines:', remaining_lines, '\n')
                        print('\t\t', size_check)

                    # clear memory/reset stuph
                    char_list.clear()
                    index = inc_index

                    if create_sample:
                        exit()

                # remove newline if present
                line = ''.join(line).replace('\n', '')

                # fill list/memory
                line_list.append(line)

            print('Done.')




        format_alg()

t4()

