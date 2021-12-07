import configparser
from os import path

config = configparser.ConfigParser()
config.optionxform = str # makes parser case-sensitive
configPath = './config.ini'

###############################################################################
# generate config file if not detected
if path.isfile(configPath) is False:
    print('Configuration file not detected, creating new one...')
    with open(configPath, 'w') as config_file:
        config['DEBUG'] = {'bEnableDebug': 'False'}
        config['INFO'] = {'bShowMemRuntime': 'True'}
        config['MISC'] = {'bCreateBackup': 'True'}
        config['RESOURCE'] = {'iFreeMemoryPercent': '70'}

        config.write(config_file)
        print('\t>>> Done.')
################################################################################

config.read(configPath)

# DEBUG
enableDebug = config.getboolean('DEBUG', 'bEnableDebug')

# INFO
showRunInfo = config.getboolean('INFO', 'bShowMemRuntime')

# MISC
enableBackup = config.getboolean('MISC', 'bCreateBackup')

# RES
free_memory_percent = config.getint('RESOURCE', 'iFreeMemoryPercent')