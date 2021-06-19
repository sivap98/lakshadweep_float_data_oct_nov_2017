# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:44:52 2021

@author: Dell
"""

import xarray as xr
import matplotlib.pyplot as plt
data = xr.open_dataset('D:/argo/aoml/2903125/2903125_prof.nc')
# Profile Plot
# Subplot example
fig, (ax1,ax2) = plt.subplots(1,2, sharey=True, figsize=(10,6))

nprof = 122 # Fist profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof = 123 # Middle-ish profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof = 124 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =125 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =126 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =127 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =128 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =129 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =130 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

nprof =131 # Last profile
ax1.plot(data.TEMP_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof], label=data.JULD[nprof].dt.strftime('%Y-%m-%d').values)
ax2.plot(data.PSAL_ADJUSTED[nprof], data.PRES_ADJUSTED[nprof])

ax1.set_ylabel('Pressure (dbar)')
ax1.set_xlabel('Temperature (C)')
ax2.set_xlabel('Salinity(psu)')
ax1.invert_yaxis()
ax1.legend()

# Add some gridlines
ax1.grid()
ax2.grid()

# Add a super title
fig.suptitle('Argo Float #%d' % data.PLATFORM_NUMBER[nprof].values, fontweight='bold', fontsize=16);