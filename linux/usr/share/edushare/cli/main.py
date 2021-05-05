#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"

"""
- Licence: Likapi Education
- Name: EduShare
- Version: 1.0
"""

#import librairies
import os, sys
from gui import *
from conf import *

#verify if this is a linux
def verifySys():
	if sys.platform == "linux" or sys.platform == "linux2":
		main()
	elif sys.platform == "darwin":
		print(GREEN + """
	Mac Os détecté, vous devez utiliser linux...
		""")
		close()
	elif sys.platform == "win32" or sys.platform == "win64":
		print(GREEN + """
	Windows détecté, vous devez utiliser linux...
		""")
		close()
	else:
		print(GREEN + """
	Impossible d'identifier le système d'exploitation...
		""")
		close()

#start program
if __name__ == "__main__":
	verifySys()