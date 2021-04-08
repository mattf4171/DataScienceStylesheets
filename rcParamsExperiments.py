#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:14:49 2021

@author: matthewfernandez
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


IPython_default = plt.rcParams.copy()
from matplotlib import cycler

colors = cycler('color', 
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow = True, grid=True, prop_cycle=colors)
plt.rc('xtick', direction='out', color ='gray')
plt.rc('ytick', direction='out', color ='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)




for i in range(4):
    plt.plot(np.random.rand(10))