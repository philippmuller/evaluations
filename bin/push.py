#!/usr/bin/env python
""" Push to all from remote repositories.
"""

# standard library
import argparse
import os

''' Functions
'''
def push():
    """ Push all remote repositories.
    """
    print('\n.. pushing ')

    os.system("git clean -f") 

    os.system("git commit -a -m'committing'") 

    os.system("git push")

''' Execution of module as script
'''
if __name__ == '__main__':

    parser  = argparse.ArgumentParser(description = \
        'Push to all remote repositories.',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    args = parser.parse_args()

    push()
