'''
Created on Aug 16, 2014

Simple encapsulation of the result of a "command" that may include errors
Typically used for command line functions that can be composed easily

@author: Stan
'''

import sys

# expected values for error_code
ERROR_UNDEFINED = -1  # error code meaning "command did not set errorcode"
ERROR_SUCCESS = 0  
ERROR_INVALID_INPUT = 1  # user input is not valid
ERROR_FAILED = 2  # failed.  If possible, set the exception as well 

ERROR_STRINGS = {ERROR_UNDEFINED : "undefined",
                 ERROR_SUCCESS : "Success",
                 ERROR_INVALID_INPUT : "Invalid Input",
                 ERROR_FAILED : "Failed" }

class CommandResult (object):
    ''' Encapsulate the result of a command action
    
    Many "action methods' can detect errors and want to report status 
    This encapsulation simplifies error handling and unit tests
    Each command is required to catch its own errors and store them here    
    '''

    def __init__(self, result = None, error_code = ERROR_UNDEFINED, 
                 error_message = None, exception = None):
        '''
        Constructor
        '''
        self.result = result
        self.error_code = error_code
        self.exception = exception
        self.error_essage = error_message
      
    @property
    def is_error(self):
        return ERROR_SUCCESS != self.error_code

    @property
    def error_message_string (self):
        '''return an error message for printing by applying some defaults across error code and result
        '''
        message = self.error_essage
        if message == None:
            if self.result != None:
                message = str(self.result)
            else:
                try:
                    self.error_essage = ERROR_STRINGS[self.error_code]
                except KeyError:
                    self.error_essage = "Error Code " + str(self.error_code)
        elif not isinstance(message, str):
            message = str(message)
        return message
    
    def print_message (self):
        '''print the message to stdout if code is success, else to stderr
        '''
        msg = self.error_message_string
        # ensure on separate line, 
        if self.is_error:
            sys.stderr.write (msg + "\n")
        else:
            sys.stdout.write (msg + "\n")
        
        
    
        