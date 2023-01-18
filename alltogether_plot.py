#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:23:24 2022

@author: maks
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.xlabel("$\Delta\sigma_8$")
plt.ylabel("Normalized distance")
plt.xlim([0.0, 0.5])
plt.ylim([0.9, 3.7])
plt.grid()
alpha=0.7
linewidth = 1

file = 'z2/dim0_order1_btstr1_portion1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#040289',alpha=alpha,linewidth=linewidth,
         label='Mean of $W_1$-distances for 0-Homologies at z=2')
plt.plot(xu*0.1, medians/medians[0], c='#9F0A64',alpha=alpha,linewidth=linewidth,
         label='Median of $W_1$-distances for 0-Homologies at z=2')
print(file)

file = 'z1/dim0_order1_btstr1_portion1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#2B4DD8',alpha=alpha,linewidth=linewidth,
         label='Mean of $W_1$-distances for 0-Homologies at z=1')
plt.plot(xu*0.1, medians/medians[0], c='#F94BE7',alpha=alpha,linewidth=linewidth,
         label='Median of $W_1$-distances for 0-Homologies at z=1')
print(file)

file = 'z01/dim0_order1_btstr1_portion1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#04CEE6',alpha=alpha,linewidth=linewidth,
         label='Mean of $W_1$-distances for 0-Homologies at z=0.1')
plt.plot(xu*0.1, medians/medians[0], c='#F19601',alpha=alpha,linewidth=linewidth,
         label='Median of $W_1$-distances for 0-Homologies at z=0.1')
print(file)


plt.legend(loc='upper left',prop={'size': 6})
plt.savefig('alltogether_normalized_.png',dpi=700)
plt.clf() 
