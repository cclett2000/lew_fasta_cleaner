from shutil import copyfile

# TODO: work on a partitioning method that divides larger files
#       so systems with less RAM can work through each partition
#       opposed to storing the entire file in RAM;

def faa_cleaner(file, debug, backup):
    # PATHs
    PATH = '.input/' + file  # retrieves file from PATH
    BKPATH = '.input/.backup/' + file # where to create backup file

    # create backup file; UPDATED - now uses buffering
    if backup is True:
        print('\n>>> Creating Backup...')

        backup_file = open(BKPATH, 'a')
        with open(PATH, buffering=2**30) as file:
            for line in file:
                backup_file.write(line)

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

def fna_reformat(file, debug, backup):
    # placeholder function for the fasta reformatter
    #   - remove all headers
    #   - format sequences so they are around 200bps
    #   - create a partitioning algorithm that allows the use
    #     of large files when sufficient RAM is not available
    #       > could use char count to estimate amount of RAM to use;

    # BACKUP

    # REPLACER/DEBUG
    pass