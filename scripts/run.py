# Charles Lett Jr.
# October 25, 2021
# main script for running FASTA file cleaner

############################################################################################
# IMPORTS

# base imports
import os
import psutil
import config
import datetime

# import created modules
from module import fasta_module

# TODO: implement memory check

############################################################################################
# MODULES
#   - WHEN IMPLEMENTING NEW MODULES, UPDATE IF STATEMENT IN 'get_module()'

module_name = {1: 'faa_cleaner',
               2: 'fna_formatter'}

module_desc = {1: '\n\t > Trims header(s) in a FASTA file containing amino acids;'
                  '\n\t   Prepares file for multiple sequence alignment.',
               2: '\n\t > Reformat a FASTA file containing nucleic acids;'
                  '\n\t   Removes all headers and makes each sequence a specific length.'}


############################################################################################
# FUNCTIONS

# scans '.input' DIR, allow user to select file
def get_file():
    # clear cmd prompt/terminal
    os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')

    print('DEBUG:', config.enableDebug, '| BK:', config.enableBackup, '| RUNINFO:', config.showRunInfo)

    print('\n>>> Scanning for files...')

    # scan '.input' dir for files
    global file_sel
    files = os.listdir(os.path.abspath('./.input'))
    dir_ind = 1

    print('  File(s) found:')
    # the extra '+ 1' & '- 1' is to ignore and not display the backup folder;
    # display found files
    for f in range(len(files) - 1):
        print('  ' + str(dir_ind) + ')', files[dir_ind])
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
            print('  ' + str(dir_ind) + ')', files[dir_ind])
            dir_ind += 1

        dir_ind = 1 # reset dir index

        # request user input (again...ugh get it right XD)
        file_num = input('\nEnter the number corresponding to the file you would like cleaned: ')
        file_num = int(file_num)  # input - str >> int


    file_sel = files[file_num]
    print('- Selected file: ' + file_sel)

# select which module to use; GLOBALS = 'processed_file', 'mod_sel', 'module_runtime'
def get_module():
    global mod_sel, processed_file, module_runtime

    os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')

    # status
    print('DEBUG:', config.enableDebug, '| BK:', config.enableBackup, '| RUNINFO:', config.showRunInfo)
    print('- Selected file: ' + file_sel)

    print('\n>>> Selecting Module...')

    # display modules and there descriptions
    print('  Available Module(s):')
    for i in module_name:
        print('  ' + str(i) + ')', module_name[i], module_desc[i])

    # display message and request user input
    mod_num = input('\nPlease enter the number corresponding to the module you would like to run: ')
    mod_num = int(mod_num) # input - str > int

    # input check
    while mod_num < 1 or mod_num > len(module_name):
        # if user input isn't available, inform of error and request again
        os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')
        print('>>> Error: the number entered is not available, please try again'
              '\nSelect from:')

        # re-display modules so user doesn't need to scroll up
        for i in module_name:
            print(' ', str(i) + ')', module_name[i], module_desc[i])

        # request user input (again...ugh get it right XD)
        mod_num = input('\nEnter the number corresponding to the module you would like to run: ')
        mod_num = int(mod_num)  # input - str >> int

    mod_sel = module_name[mod_num]

    # reset display and include selected module
    os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')
    print('DEBUG:', config.enableDebug, '| BK:', config.enableBackup, '| RUNINFO:', config.showRunInfo)
    print('- Selected file:',  file_sel)
    print('- Selected Module:', mod_sel)

    # start runtime - for modules
    time_start = datetime.datetime.now()

    # execute selected module
    if mod_sel == 'faa_cleaner':
        processed_file = fasta_module.faa_cleaner(file_sel, config.enableDebug, config.enableBackup)
    if mod_sel == 'fna_formatter':
        print('\n>>> This module is not yet implemented.'
              '\nExiting...')
        exit()

    # finish runtime - for modules
    time_end = datetime.datetime.now()  # end runtime record
    module_runtime = time_end - time_start

# writes to a new file in the '.output' folder
def write_file(file_name, file):
    PATH = '.output/' + ('EDITED_' + file_name)

    print('\n>>> Saving to file...')

    # if file exists let user know it was overwritten
    if os.path.exists(PATH):
        print('- File already exists, overwriting...')
        writer = open(PATH, 'w+') # write to file; create if not available
        writer.write(file)
        print('- Done.')
        writer.close()

    else:
        print('- Creating new file...')
        writer = open(PATH, 'w+') # write to file; create if not available
        writer.write(file)
        print('- Done.')
        writer.close()

    # for 'show_location' setting >>> later implementation of config.ini
    # print ('File Location:', os.path.abspath('EDITED_' + file_name))

############################################################################################
# FUNCTION CALLERS

get_file() # 'file_sel'; request user input for detected files
get_module() # 'processed_file'; request user module selection
write_file(file_sel, processed_file) # writes cleaned_file to new file

############################################################################################
# PROGRAM END

process = psutil.Process() # get process ID?

#TODO: fix memory usage - only records memory used before program finished
#TODO: rework runtime recorder

print('\nProgram Finished.')
# runtime may not be accurate :-/ >>> make sure to start runtime calc after user input
if config.showRunInfo:
    print('- Runtime:', int(module_runtime.total_seconds() * 1000), 'ms')
    print('- Memory Usage:', process.memory_info().rss/10**6, 'MB\n') # show memory usage? just playing around here