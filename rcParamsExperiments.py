#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:14:49 2021

@author: matthewfernandez
Description: Explore some different stylesheets for a histogram and line plot
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
    
    
plt.style.available[:5] # view the available top 5 stylesheets

def hist_and_lines():
    # fn to create two basic types of plots
    np.random.seed(0)
    fig, ax= plt.subplots(1,2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a','b', 'c'], loc='lower left')

with plt.style.context('fivethirtyeight'): 
    # fivethirtyeight will incorporate bold colors, thick lines and transparent axes
    hist_and_lines()



with plt.style.context('ggplot'): 
    # ggplot resembles R lang vizualization tool, mimics default style from that pkg
    hist_and_lines()
    
    
with plt.style.context('bmh'):
    # bmh stylesheet mimics the 'Probabilistic Programming and Bayesian Methods 
    # for Hackers' with rcParams to create consistent and visually appealing styles
    hist_and_lines()
    
    
with plt.style.context('dark_background'):
    # Great for presentations, useful with dark backgrounds
    hist_and_lines()
    
with plt.style.context('grayscale'):
    # great when printed w/o color
    hist_and_lines()
    
    
    
    
