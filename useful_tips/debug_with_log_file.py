"""
Use the logging module instead of the print() function to debug with messages.
Thanks to this, one can immediately know the output from normal program
execution and the output from debugging.
"""

import logging

logging.basicConfig(filename="logs.txt", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Put this in place where you want obtain information.
logging.debug("This is diagnostic message.")

# Example output in 'logs.txt'.
# 2022-11-19 17:23:43,655 - DEBUG - This is diagnostic message.
