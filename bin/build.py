#!/usr/bin/env python
''' Quick script to build the refereeing documents.
'''

# project library
from _auxiliary import *

# global variables
DOCUMENTS = ['doc']

''' Execution of module as script.
'''
if __name__ == '__main__':
    
	
    
    # Compile documents.
    for type_ in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:

        for document in DOCUMENTS:
            
            run(type_, document)
            
    # Copying of files.
    for document in DOCUMENTS:
        
        copy(document)   

    # Finishing.
    cleanup(all_ = False) 