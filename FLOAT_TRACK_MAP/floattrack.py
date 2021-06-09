# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:11:50 2021

@author: Dell
"""

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
data = xr.open_dataset('D:/argo/incois/2901307/2901307_prof.nc')

# Simple map of a float track
plt.figure(figsize=(8,6))
plt.plot(data.LONGITUDE, data.LATITUDE, c='lightgrey')
plt.scatter(data.LONGITUDE, data.LATITUDE, c=data.JULD, cmap='RdYlBu')

# Crude profile labels
for jj in [238,241]:
  plt.text(data.LONGITUDE[jj]+.02, data.LATITUDE[jj]+.02, data.N_PROF[jj].values)

# Add a colorbar
cbar = plt.colorbar();

# Fix the colorbar ticks
import pandas as pd # We need pandas for this
cbar.ax.set_yticklabels(pd.to_datetime(cbar.get_ticks()).strftime(date_format='%Y-%m-%d'));

# Set the aspect ratio to pseudo-Mercator
plt.gca().set_aspect(1 / np.cos(np.deg2rad( np.mean(plt.ylim()) )))