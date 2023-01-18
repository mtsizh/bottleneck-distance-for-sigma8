#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:23:24 2022

@author: maks
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.xlabel("$\Delta_{\sigma_8}$")
plt.ylabel("Normalized distance")
plt.xlim([0.0, 0.5])
plt.ylim([0.9, 3.5])
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
plt.plot(xu*0.1, means/means[0], c='#FF5555',alpha=alpha,linewidth=linewidth,
         label='0-Homologies, no bootstrap')
print(file)

file = 'z2/dim0_order1_btstr3_portion0.3'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#FF5555',alpha=alpha,linewidth=linewidth,
         linestyle='--',
         label='0-Homologies, 3x bootstrap')
print(file)

file = 'z2/dim0_order1_btstr5_portion0.2'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#FF5555',alpha=alpha,linewidth=linewidth,
         linestyle='-.',
         label='0-Homologies, 5x bootstrap')
print(file)

file = 'z2/dim0_order1_btstr10_portion0.1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#FF5555',alpha=alpha,linewidth=linewidth,
         linestyle=':',
         label='0-Homologies, 10x bootstrap')
print(file)

###############################################################################
file = 'z2/dim1_order1_btstr1_portion1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#5555FF',alpha=alpha,linewidth=linewidth,
         label='1-Homologies, no bootstrap')
print(file)

file = 'z2/dim1_order1_btstr3_portion0.3'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#5555FF',alpha=alpha,linewidth=linewidth,
         linestyle='--',
         label='1-Homologies, 3x bootstrap')
print(file)

file = 'z2/dim1_order1_btstr5_portion0.2'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#5555FF',alpha=alpha,linewidth=linewidth,
         linestyle='-.',
         label='1-Homologies, 5x bootstrap')
print(file)

file = 'z2/dim1_order1_btstr10_portion0.1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#5555FF',alpha=alpha,linewidth=linewidth,
         linestyle=':',
         label='1-Homologies, 10x bootstrap')
print(file)

###############################################################################

file = 'z2/dim2_order1_btstr1_portion1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#55FF55',alpha=alpha,linewidth=linewidth,
         label='2-Homologies, no bootstrap')
print(file)

file = 'z2/dim2_order1_btstr3_portion0.3'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#55FF55',alpha=alpha,linewidth=linewidth,
         linestyle='--',
         label='2-Homologies, 3x bootstrap')
print(file)

file = 'z2/dim2_order1_btstr5_portion0.2'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#55FF55',alpha=alpha,linewidth=linewidth,
         linestyle='-.',
         label='2-Homologies, 5x bootstrap')
print(file)

file = 'z2/dim2_order1_btstr10_portion0.1'
data = pd.read_csv(file+'.csv')
y = np.array(data['Distance'])
x = np.array(data['deltasigma8'])
xu = np.unique(x)
means = [np.mean(y[x == xv]) for xv in xu]
medians =  [np.median(y[x == xv]) for xv in xu]
plt.plot(xu*0.1, means/means[0], c='#55FF55',alpha=alpha,linewidth=linewidth,
         linestyle=':',
         label='2-Homologies, 10x bootstrap')
print(file)


plt.legend(loc='upper left',prop={'size': 6})
plt.savefig('bootstrapped.png',dpi=700)
plt.clf() 
