# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:00:57 2019

@author: sachi
"""

import pandas as pd

import_file = pd.read_csv("D:\Data Science\Python_Files\Simple linear regression.csv")

print import_file

import_file.to_csv("D:\Data Science\Python_Files\Simple linear regression.csv")