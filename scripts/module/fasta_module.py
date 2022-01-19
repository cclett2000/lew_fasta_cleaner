import os
from multiprocessing import Process

def faa_head_cleaner(file, debug, backup, buffer_size):
    # PATHs
    PATH = '.input/' + file  # retrieves file from PATH
    WRPATH = '.output/EDITED_' + file
    BKPATH = '.input/.backup/' + file # where to create backup file

    # create backup file; UPDATED - now uses buffering
    if backup is True:
        print('\n>>> Creating Backup...')

        backup_file = open(BKPATH, 'a')
        with open(PATH, buffering=buffer_size) as file:
            for line in file:
                backup_file.write(line)

        print('- Done.')

    else:
        print('\n>>> File Backup Disabled.')

    # start cleaner
    print("\n>>> 'faa_cleaner' starting...")

    if os.path.exists(WRPATH):
        print('- Output File Already Exists. Removing...', end='\a')
        os.remove(WRPATH)
        print('Done!')

    with open(PATH, buffering=buffer_size) as file:
        write_file = open(WRPATH, 'a')
        line_store = []
        status_message = ['- Status: Cleaning...',
                          '- Status: Writing... ',
                          '- Status: Done.      ']
        status = status_message[0]

        # shows/updates to display whats occurring
        def show_status(status):
            print(status, end='\r')
        show_status(status)

        # store headers in list, with its pos
        start = 0
        end = 0
        seq_count = 0

        for line in file:
            if line[0] == '>':
                start = 1  # set start to line ind. with '>'

                for j in range(len(line)):
                    if line[j] == '_':
                        end = j + 1 # set end to first '_'
                        break

                # store header in 'header' list; clean if needed
                if debug is True:
                    seq_count += 1 # increment to find number of headers
                    # shows debug info to help solve any future issues
                    print('\nHEADER/SEQ #:', seq_count)
                    print('START:', start, '| END:', end)  # start/end pos within head
                    print('\nBEF:', line)  # before replace
                    if end < 30:
                        line = line.replace(line[start:end], '')
                    print('AFT:', line) # after replace
                    print('-'*30)

                elif debug is False:
                    # buffering isn't being utilize but the 1MIL check works!
                    # ^ will not write small files :(
                    if end < 30:
                        # big data check (uses ~2.7GB of RAM)
                        while len(line_store) > 10000000:
                            status = status_message[1] # update status -writing
                            show_status(status)

                            write_file.write(''.join(line_store))

                            status = status_message[0] # update status -we're back to cleanin!
                            show_status(status)

                            line_store.clear() # purge list
                        line = line.replace(line[start:end], '')

            line_store.append(line)

    # write to file if file was able to fit within list constraint
    if len(line_store) < 10000000:
        status = status_message[1]  # update status -writing
        show_status(status)
        write_file.write(''.join(line_store))

    status = status_message[2]  # update status -complete
    show_status(status)
    print("\n- Complete.")

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