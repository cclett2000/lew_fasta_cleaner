from shutil import copyfile

def file_cleaner(file, debug, backup):
    # PATHs
    PATH = '.input/' + file  # retrieves file from PATH
    BKPATH = '.input/.backup/' + file # where to create backup file

    # create backup file
    if backup is True:
        print('\n>>> Creating Backup...')
        copyfile(PATH, BKPATH)  # copy file to BKPATH
        print('- Done.')
    else:
        print('\n>>> File Backup Disabled.')

    # start cleaner
    print('\n>>> Cleaning File...')

    with open(PATH) as file:
        lines = file.readlines()

        # store headers in list, with its pos
        start = 0
        end = 0
        seq_count = 0
        for i in range(len(lines)):
            if lines[i][0] == '>':
                start = 1  # set start to line ind. with '>'

                for j in range(len(lines[i])):
                    if lines[i][j] == '_':
                        end = j + 1 # set end to first '_'
                        break

                # store header in 'header' list; clean if needed
                if debug is True:
                    seq_count += 1 # increment to find number of headers
                    # shows debug info to help solve any future issues
                    print('\nHEADER/SEQ #:', seq_count)
                    print('\nHEADER_LINE_POS:', i + 1, '\n')  # head pos
                    print('START:', start, '| END:', end)  # start/end pos within head
                    print('\nBEF:', lines[i])  # before replace
                    if end < 30:
                        lines[i] = lines[i].replace(lines[i][start:end], '')
                    print('AFT:', lines[i]) # after replace
                    print('-'*30)

                elif debug is False:
                    if end < 30:
                        lines[i] = lines[i].replace(lines[i][start:end], '')

        # print("".join(lines)) # uncomment to see if file came together properly


    print("- Done.")
    return "".join(lines)
