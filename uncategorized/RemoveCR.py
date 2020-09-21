#!/usr/bin/env python

"""

[ RemoveCR.py ]

	- This program is to remove carriage returns hidden in each lines.
	  The carriage returns must have been made in windows environment.

	- Env : Python 2.7.17

"""

print '[ Remove Carriage Return ]'

orig_name = raw_input('Input src file name : ')
target_name = raw_input('Input dst file name : ')

try:
	with open (orig_name, 'rb') as orig_file:
		with open(target_name, 'wb') as target_file:
			for line in orig_file.readlines():
				target_file.write(line.replace('\r', ''))

except IOError as ioe:
	print 'IOError occurred.. Check the target files...'
except:
	print 'Uexpected error...'
else:
	print 'Done!'
