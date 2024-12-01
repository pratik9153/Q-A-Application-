import sys
import traceback

class customexception(Exception):
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        
        # Extract traceback information
        _, _, exc_tb = error_details.exc_info()
        
        # Get the line number and file name
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Catch the exception and raise custom exception
        raise customexception(e, sys)  # Pass sys as the error_details
