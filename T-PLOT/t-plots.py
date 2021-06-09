# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:42:20 2021

@author: Dell
"""

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
data = xr.open_dataset('D:/argo/aoml/2903125/2903125_prof.nc')

data.TEMP_ADJUSTED.T.plot()
plt.gca().invert_yaxis()
plt.title('2901325')