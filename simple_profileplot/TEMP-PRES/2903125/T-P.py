# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:11:17 2021

@author: Dell
"""

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
data = xr.open_dataset('D:/argo/incois/2901307/2901307_prof.nc')

nprof = 241 #Specify a profile to plot
plt.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

plt.xlabel('Temperature(C)')
plt.ylabel('Pressure (dbar)')
plt.title('Argo Profile from %s' % data.JULD[nprof].dt.strftime('%a, %b %d %H:%M').values)

plt.gca().invert_yaxis() #Flip the y-axis