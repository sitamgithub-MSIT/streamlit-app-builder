"""
This module defines a custom exception handling class and a function to get error message with details of the error.
"""

# Standard Library
import sys

# Local imports
from src.logger import logging


# Function Definition to get error message with details of the error (file name and line number) when an error occurs in the program
def get_error_message(error, error_detail: sys):
    """
    Get error message with details of the error.

    Args:
        - error (Exception): The error that occurred.
        - error_detail (sys): The details of the error.

    Returns:
        str: A string containing the error message along with the file name and line number where the error occurred.
    """
    _, _, exc_tb = error_detail.exc_info()

    # Get error details
    file_name = exc_tb.tb_frame.f_code.co_filename
    return "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )


# Custom Exception Handling Class Definition
class CustomExceptionHandling(Exception):
    """
    Custom Exception Handling:
        This class defines a custom exception that can be raised when an error occurs in the program.
        It takes an error message and an error detail as input and returns a formatted error message when the exception is raised.
    """

    # Constructor
    def __init__(self, error_message, error_detail: sys):
        """Initialize the exception"""
        super().__init__(error_message)

        self.error_message = get_error_message(error_message, error_detail=error_detail)

    def __str__(self):
        """String representation of the exception"""
        return self.error_message
