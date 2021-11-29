import datetime
import psutil

available_memory_B = psutil.virtual_memory().available
available_memory_GB = psutil.virtual_memory().available / 10**9
print('Available Memory: GByte = ', available_memory_GB, ' Byte =', available_memory_B)

test_buffer = 2**30
print('Buffer: GByte =', (test_buffer / 10**9), ' Byte =', test_buffer)

mem_threshold_B = 536870912 # 512 megabytes

time_start = datetime.datetime.now()


with open('../.input//A3_S1_LALL_R1_001(2).fasta') as file:
    pass

time_end = datetime.datetime.now()  # end runtime record
module_runtime = time_end - time_start
print('- Runtime:', int(module_runtime.total_seconds() * 1000), 'ms')

