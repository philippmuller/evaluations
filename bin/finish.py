#!/usr/bin/env python
''' Quick script to finish the refereeing process.
'''

# standard library
import shutil
import os

# Build documents.
os.system('./build')

# Store documents.
for src in ['ref-letter.pdf', 'ref-report.pdf']:
	
	dst = 'dist/' + src

	shutil.copy(src, dst)

# Clean documents.
os.system('./clean')