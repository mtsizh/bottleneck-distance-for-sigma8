#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:48:26 2022

@author: maks
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

directory='z2'
for file in glob.glob(directory+"/*.csv"):
#filename = 'massfiltz01/dim1_order1_btstr5_portion0.2'
#filename = 'z2/dim1_order1_btstr1_portion1'
    data = pd.read_csv(file)
#    plt.scatter(data['deltasigma8'].to_numpy()*0.1,data['Distance'].to_numpy() ,s=5)
    plt.xlabel("sigma8 delta")
    plt.ylabel("bottleneck distance")

    y = np.array(data['Distance'])
    x = np.array(data['deltasigma8'])
    xu = np.unique(x)
    means = [np.mean(y[x == xv]) for xv in xu]
#    plt.boxplot([y[x == xv] for xv in xu], showmeans=True, positions=xu/10, widths=0.02)
#    plt.plot(xu*0.1, means, c='r')    
    plt.plot(xu*0.1, means/means[0], c='r')   
    plt.xlim([-0.1, 0.6])
    plt.grid()
    print(file)
    plt.savefig(file[:len(file)-4] + '_normalized.png',dpi=700)
#    plt.savefig(file[:len(file)-4]+'.png',dpi=700)

    plt.clf() 


