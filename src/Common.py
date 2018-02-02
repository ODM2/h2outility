"""

Contains constants and other common variables

"""

import os
import sys
import inspect
import re


class Common:
    def __init__(self, args):
        """
        Set up values that are globally accessible
        """
        self.H2O_DEBUG = True if '--debug' in args else False       # If true, run in debug mode
        self.VERBOSE = True if '--verbose' in args else False       # Print additional log messages
        self.TEST_H2O = True if '--test_h2o' in args else False     # Used to quickly test repetitive GUI portions
        self.DELETE_RESOURCE_FILES = True if '--delete_existing_resource_files' in args else False  # Delete all files in HydroShare resource before upload
        self.SET_RESOURCES_PUBLIC = True if '--make_resources_public' in args else False    # Set all modified resources to public
        self.SKIP_QUERIES = True if '--skip_queries' in args else False         # Do not query data for CSV files
        self.SKIP_HYDROSHARE = True if '--skip_hydroshare' in args else False   # Do not modify HydroShare resources

        """
        General constants and non-class variables
        """
        settings_file = 'operations_file.json'                                  # Default settings file name
        for item in args:
            if '--settings_file=' in item:
                settings_file = item.split('--settings_file=')[1]

        self.IS_WINDOWS = 'nt' in os.name
        self.APP_LOCAL = os.getenv('LOCALAPPDATA')
        self.PROJECT_DIR = str(os.path.dirname(os.path.realpath(__file__)))      # Root project directory
        self.USER_APP_DIR = '{}/h2o_utility'.format(self.APP_LOCAL)
        self.SETTINGS_FILE_NAME = self.USER_APP_DIR + '/' + settings_file        # Settings file name
        self.DATASET_DIR = '{}/H2O_dataset_files/'.format(self.USER_APP_DIR)     # Directory for generated CSV files
        self.LOGFILE_DIR = '{}/logs/'.format(self.USER_APP_DIR)                  # Directory for log files
        self.GUI_MODE = False                                                    # If true, send logs to GUI

        """
        H2O-specific constants
        """
        self.CSV_COLUMNS = ["LocalDateTime", "UTCOffset", "DateTimeUTC"]    # Columns shared by QC0, QC1 CSV files
        self.QUERY_CHUNK_SIZE = 250000 if not self.TEST_H2O else 10         # Get query results in chunks to prevent out of memory errors
        self.DATAVALUES_TIMEOUT = 6                                         # Query timeout for data values (not implemented)
        self.SERIES_TIMEOUT = 5                                             # Query timeout for data series (not implemented)

        """
        Setup sys and other args
        """
        sys.path.append(os.path.dirname(self.PROJECT_DIR))

    def dump_settings(self):
        for key in self.__dict__:
            print '{:<35} {}'.format(str(key) + ':', self.__dict__[key])


"""

Functions used among H2O Services

"""


def GetSeriesColumnName(series):
    """
    Prints useful information for a given series object.
    """
    return '{} & {} & QC {}'.format(series.site_code, series.variable_code, series.quality_control_level_code)


def InitializeDirectories(directory_list):
    """
    Creates directories if they do not exist.
    """
    for dir_name in directory_list:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


def PRINT_NAME_VALUE(name, var):
    """
    Print variable and variable name.
    """
    print '{}: {}'.format(name, var)


# noinspection PyUnusedLocal
def varname(p):
    """
    Returns the variable name, useful when printing lots of variables and don't want to name them all
    """
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


def print_metadata(value):
    """
    Print metadata, used for debugging
    """
    print '\nHydroShare metadata:'
    print print_recursive(value)


def print_recursive(value, indent=0):
    """
    Oddly complex way to print data structures in a readable way
    """
    tabs = lambda count: '' + str('    ' * (indent + count))
    if isinstance(value, dict):
        to_print = '{}{}'.format(tabs(1), '{')
        for key, item in value.iteritems():
            to_print += '\n{}{}:\n{}'.format(tabs(2), key, print_recursive(item, indent + 2))
        return to_print + '{}{}'.format('\n' + tabs(1) if len(value) > 0 else ' ', '}')
    if isinstance(value, list):
        to_print = '{}['.format(tabs(1))
        for item in value:
            to_print += '\n' + print_recursive(item, indent + 1)
        return to_print + '{}{}'.format('\n' + tabs(1) if len(value) > 0 else ' ', ']')
    if isinstance(value, str) or isinstance(value, unicode):
        return tabs(1) + '\'' + value + '\''
    if len(str(value)) > 0:
        return tabs(1) + str(value) + ''
    return ''


APP_SETTINGS = Common(sys.argv)  # Global app settings
