# Charles Lett Jr.
# October 25, 2021
# main script for running FASTA file cleaner
# TODO: fix bug with DIR PATH
#       fix bug with 'config.ini' not returning what is set;
import os
import psutil
import config
import cleaner
import datetime

# scans '.input' DIR then asks for user input
def get_file():
    # clear cmd prompt/terminal
    os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')

    print('DEBUG:', config.enableDebug, '| BK:', config.enableBackup, '| RUNINFO:', config.showRunInfo)

    print('\n>>> Scanning for files...')

    # scan '.input' dir for files
    global file_sel
    files = os.listdir(os.path.abspath('./.input'))
    dir_ind = 1

    print('File(s) found:')
    # the extra '+ 1' & '- 1' is to ignore and not display the backup folder;
    # display found files
    for f in range(len(files) - 1):
        print('- ' + str(dir_ind) + ')', files[dir_ind])
        dir_ind += 1

    dir_ind = 1 # reset dir index

    # display message and request user input
    file_num = input('\nPlease enter the number corresponding to the file '
                     'you would like cleaned: ')
    file_num = int(file_num) # input - str > int

    # input check
    while file_num <= 0 or file_num >= len(files):
        # if user input isn't available, inform of error and request again
        os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')
        print('>>> Error: the number entered is not available, please try again'
              '\nSelect from:')

        # re-display files so user doesn't need to scroll up
        for f in range(len(files) - 1):
            print('- ' + str(dir_ind) + ')', files[dir_ind])
            dir_ind += 1

        dir_ind = 1 # reset dir index

        # request user input (again...ugh get it right XD)
        file_num = input('\nEnter the number corresponding to the file you would like cleaned: ')
        file_num = int(file_num)  # input - str >> int


    file_sel = files[file_num]
    print('- Selected file: ' + file_sel)

# writes the cleaned file to a new file in the '.output' folder
def write_file(file_name, cleaned_file):
    PATH = '.output/' + ('EDITED_' + file_name)

    print('\n>>> Saving to file...')

    # if file exists let user know it was overwritten
    if os.path.exists(PATH):
        print('- File already exists, overwriting...')
        writer = open(PATH, 'w+') # write to file; create if not available
        writer.write(cleaned_file)
        print('- Done.')
        writer.close()

    else:
        print('- Creating new file...')
        writer = open(PATH, 'w+') # write to file; create if not available
        writer.write(cleaned_file)
        print('- Done.')
        writer.close()

    # for 'show_location' setting >>> later implementation of config.ini
    # print ('File Location:', os.path.abspath('EDITED_' + file_name))

############################################################################################

# program start
get_file() # 'file_sel'; request user input for detected files

time_start = datetime.datetime.now() # start runtime record
process = psutil.Process() # get process ID?

# call functions
cleaned_file = cleaner.file_cleaner(file_sel, config.enableDebug, config.enableBackup) # holds cleaned file
write_file(file_sel, cleaned_file) # writes cleaned_file to new file

# program finish
time_end = datetime.datetime.now() # end runtime record
runtime = time_end - time_start

print('\nProgram Finished.') # finish message

# debugging
# runtime may not be accurate :-/ >>> make sure to start runtime calc after user input
if config.showRunInfo:
    print('- Runtime:', int(runtime.total_seconds() * 1000), 'ms')
    print('- Memory Usage:', process.memory_info().rss/10**6, 'MB\n') # show memory usage? just playing around here