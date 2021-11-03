from shutil import copyfile
import os
import psutil

def file_cleaner(file):
    # programmer options
    enable_cleaner_debug = False

    # PATHs
    PATH = '.input/' + file  # retrieves file from PATH
    BKPATH = '.input/.backup/' + file # where to create backup file

    # create backup file
    def backup_file(file):
        print('\nCreating Backup...')
        copyfile(PATH, BKPATH)  # copy file to BKPATH
        print('\t>>> Backup Finished!')
    backup_file(file)

    # start cleaner
    print('\nStarting File Cleaner...')

    with open(PATH) as file:
        lines = file.readlines()

        # store headers in list, with its pos
        start = 0
        end = 0
        for i in range(len(lines)):
            if lines[i][0] == '>':
                start = 1  # set start to line ind. with '>'

                for j in range(len(lines[i])):
                    if lines[i][j] == '_':
                        end = j + 1 # set end to first '_'
                        break

                # store header in 'header' list; clean if needed
                if enable_cleaner_debug is True:
                    # shows debug info to help solve any future issues
                    print('\nHEADER_LINE_POS:', i + 1, '\n')  # head pos
                    print('START:', start, '| END:', end)  # start/end pos within head
                    print('\nBEF:', lines[i])  # before replace
                    if end < 30:
                        lines[i] = lines[i].replace(lines[i][start:end], '')
                    print('AFT:', lines[i]) # after replace
                    print('-'*30)

                elif enable_cleaner_debug is False:
                    if end < 30:
                        lines[i] = lines[i].replace(lines[i][start:end], '')

        # print("".join(lines)) # uncomment to see if file came together properly

    # preprocess
    print("\t>>> File Cleaning Finish!")
    return "".join(lines)
