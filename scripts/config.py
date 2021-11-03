import configparser
from os import path

config = configparser.ConfigParser()
config.optionxform = str # makes parser case-sensitive
configPath = '..//config.ini'

###############################################################################
# generate config file if not detected
if path.exists(configPath) is False:
    print('Configuration file not detected, creating new one...')
    with open(configPath, 'w') as config_file:
        # config['PATH'] = {'sInpPath': '".input" folder path goes here',
        #                   'sOutPath': '".output" folder path goes here'}
        config['DEBUG'] = {'bEnableDebug': 'False'}
        config['INFO'] = {'bShowMemRuntime': 'True'}
        config['MISC'] = {'bCreateBackup': 'True'}

        config.write(config_file)
        print('\t>>> Done.')

config.read(configPath)

################################################################################

# PATH >> no longer needed
# inputPath = config.get('PATH', 'sInpPath')
# outPath = config.get('PATH', 'sOutPath')

# DEBUG
enableDebug = config.getboolean('DEBUG', 'bEnableDebug')

# INFO
showRunInfo = config.getboolean('INFO', 'bShowMemRuntime')


