# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:51:11 2019

@author: sachi
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv("D:\Data Science\Python_Files\Admittance.csv")

#print data

raw_data = data.copy()

data['Admitted'] = data['Admitted'].map({"Yes":1,"No":0})

# Assign y and x variable

y = data['Admitted']
x1 = data['SAT']
x = sm.add_constant(x1)

results = sm.OLS(y,x).fit()

print "\nparams[0] : ",results.params[0]
print "\nparams[1] : ",results.params[1]

print results.summary()

#print "Value : ",x

plt.scatter(x1,y)

reg_log = sm.Logit(y,x).fit()

print "Logit Param[0] : ",reg_log.params[0]