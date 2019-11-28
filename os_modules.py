# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:35:13 2019

@author: sachi
"""

import os

#print (dir(os))

print (os.name)
print(os.environ)
print(os.getenv)
#print(os.getlogin())
#print(os.getppid)
print(os.getcwd())
#os.mkdir('D:\Data Science\Python_Files\OS_Created_Dir')
#os.mkdir('OS_Dir_2')
os.chdir('D:\Data Science\Python_Files')
os.path.abspath('Python_Files')
#print(os.getcwd())