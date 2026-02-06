import sys
from src.logger import logging


def error_message_detail(error):
    """
    Returns a detailed error message including file name and line number.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()  # get current exception info

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = 0

    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
