# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:44:37 2021

@author: Dell
"""

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
data = xr.open_dataset('D:/argo/aoml/2903125/2903125_prof.nc')

# T-S Diagram with depth
plt.figure(figsize=(8,6))

nprof = 131 #Selected profile
plt.scatter(data.PSAL_ADJUSTED[nprof], data.TEMP_ADJUSTED[nprof])
plt.xlabel('Salinity(psu)');
plt.ylabel('Temperature (°C)')

plt.grid()

plt.title('Argo Float #%d on %s' % (data.PLATFORM_NUMBER[nprof].values, data.JULD[nprof].dt.strftime('%Y-%m-%d').values), fontweight='bold')