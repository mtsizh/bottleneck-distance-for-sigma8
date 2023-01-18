#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 01:59:51 2022

@author: maks
"""

import time
start_time = time.time()
import gudhi, gudhi.hera, os, re
import numpy as np
import pandas as pd 
from gudhi.dtm_rips_complex import DTMRipsComplex
from functools import lru_cache
from glob import glob

#input parameters
#dataleft=1
#bootstraps=1
dataleft=0.3
bootstraps=3
dimlist = [0]
orderlist = [2]

def read_all_data(file_name):
  result = []
  with open(file_name, 'r', encoding="ISO-8859-1") as file:
    for line in file:
      try:
        nums = [float(s) for s in line.split()]
      except:
        continue
      if len(nums) != 12:
       continue
      if not np.isfinite(np.sum(nums[:3])):
        continue
      result.append(nums[:3])
  return np.array(result)

@lru_cache(None)
def read_bootstrapped(file_name, seed, threshold):
    data = read_all_data(file_name)
    np.random.seed(seed)
    return data[np.random.rand(data.shape[0]) < threshold]

@lru_cache(None)
def read_intervals(filename, dim, seed, threshold):
    points = read_bootstrapped(filename, seed, threshold)
    I = get_persistence_intervals(points,dim)
    return I

def get_persistence_intervals(point_set, dim):
    alpha_complex = gudhi.AlphaComplex(points=point_set)
    simplex_tree = alpha_complex.create_simplex_tree(default_filtration_value=False)
    simplex_tree.compute_persistence()
    persistence_intervals = simplex_tree.persistence_intervals_in_dimension(dim)
    return persistence_intervals

def bottle_neck(file1, file2, dim, seed_num, threshold, order):
    dists_bootstr = []
    for seed1 in range(seed_num):
        I1 = read_intervals(file1, dim, seed1, threshold)
        for seed2 in range(seed_num):
            I2 = read_intervals(file2, dim, seed2, threshold)
            if order==100:
                dist = float(gudhi.bottleneck_distance(np.array(I1), np.array(I2)))
            else:
                dist = float(gudhi.hera.wasserstein_distance(np.array(I1), np.array(I2), order))
            dists_bootstr.append(dist)
    return np.mean(dists_bootstr)

    
#read data files
root_folder = "alldata2/z01"
dat_files = [y for x in os.walk(root_folder) for y in glob(os.path.join(x[0], '*.dat'))]
dat_files.sort()
reg_expr = '.*\/([0-9]+)groups_([0-9]+)_new.dat'
files = [{'name': f, 'param': int(re.match(reg_expr, f).group(1)), 
          'red_shift': int(re.match(reg_expr, f).group(2))} for f in dat_files]
print(files)

for dim in dimlist:
    for order in orderlist:
          delta_param = []
          d_bottle = []
          for file1 in files:
            for file2 in files:
              if file2['param'] < file1['param']:
                 continue
              if file2['name'] == file1['name']:
                 continue
              d = bottle_neck(file1['name'],
                              file2['name'],
                              dim,
                              bootstraps,
                              dataleft,
                              order)                              
              delta_param.append(np.abs(file1['param'] - file2['param']))
              d_bottle.append(d)
          df = pd.DataFrame(list(zip(d_bottle, delta_param)),
                       columns =['Distance', 'deltasigma8'])
          print('dim=',dim,'order=',order,'btstrp=',bootstraps,'portion=',dataleft, ' is saved')
          df.to_csv('z01/dim'+str(dim)+
                     '_order'+str(order)+'_btstr'+str(bootstraps)+'_portion'+str(dataleft)+'.csv')
    print('dim', dim, ' done')

print("--- %s seconds ---" % (time.time() - start_time))