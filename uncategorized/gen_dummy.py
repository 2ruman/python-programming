#!/usr/bin/env python
"""

[ gen_dummy.py ]

	This program is to generate a dummy file made up of random values.

"""
import os

with open('dummy', 'wb') as fout:
	fout.write(os.urandom(1 * 1024 * 1024 * 1024))
fout.close
