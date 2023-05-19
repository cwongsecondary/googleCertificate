#!/usr/bin/env python

import sys
import os
import re

"""
1 - Write a function that searches through log_file.  Prompts user 'What is the error?".  Store any errors in a list '[]'.  Open a file as 'r' perms with encoding='UTF-8'.  Loop through each lines in that file(readlines()).  Place 'error' list element into 'error_patterns'.  Loop the length of the error string. and append it to 
error_patterns, lowercase, split it by ' ' (error.split()).  Loop through error_pattens, return returned_errors.append(log), if re.search error_pattern is True.
2 - Write file_output function that takes param 'returned_errors'.  Open errors_found.log file as 'w' perm.  Loop through each error in returned_errors and then write to file.  Then close file.
3 - Write a __name__ == "__main__".  Assign log_file with sys.argv[1], returned_errors = error_search(log_file), 
Call file_output(passing returned_errors), Call the exit function (sys.exit(0)).
4 - Call this script (find_error.py) against working_directory/fishy.log.  


"""


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)

    file.close()
    return returned_errors

def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
    file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)


#CRON ERROR Failed to start
#./find_error.py ~/data/fishy.log
