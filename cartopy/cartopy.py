# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:18:00 2021

@author: Dell
"""

import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
data = xr.open_dataset('/content/2903125_prof.nc')
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.feature import NaturalEarthFeature,OCEAN

fig = plt.figure(figsize=(6.4,4.8),dpi=150)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([60, 74.5, 0, 20])
plt.title('2903125')
# Basemaps
states = NaturalEarthFeature(category="cultural", scale="10m",
                             facecolor="none",
                             name="admin_1_states_provinces_shp")

ax.coastlines('50m', linewidth=1)
ax.add_feature(OCEAN)
#ax.drawparallels(parallels,labels=[True,False,False,False])
#ax.drawmeridians(meridians,labels=[False,False,False,True])
ax.plot(data.LONGITUDE, data.LATITUDE, linewidth=1, color='green')