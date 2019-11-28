# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:58:09 2019

@author: sachi
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

raw_data = pd.read_csv("D:\Data Science\Python_Files\Admittance.csv")

data = raw_data.copy()

#print data

data['Admitted'] = data['Admitted'].map({'Yes':1,'No':0})

print data

y = data['Admitted']
x1 = data['SAT']
x = sm.add_constant(x1)

print x

reg_log = sm.Logit(y,x)
result_log = reg_log.fit()

print result_log.summary()

