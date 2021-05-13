# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:35:07 2021

@author: Dell
"""

import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import datetime,timedelta
import pandas as pd

dates=[]
months=[]
#importing all nc files

data=Dataset(r'D:/myi/lakshadweep/my_lakshadweep.nc')
#listing dates
sec=data.variables['TIME'][:]
ref_date=datetime(2017,10,3,7,33,27)
m=np.arange(518)
for i in m:
    date=ref_date+timedelta(seconds=float(sec[i]))
    dates.append(date)
    months.append(date.month)
#listing latitude and longitude    
lats=data.variables['LATITUDE'][:]
lons=data.variables['LONGITUDE'][:]
float_id=data.variables['PLATFORM_NUMBER']
#basemap setup            
mp=Basemap(projection="merc",llcrnrlat=9,llcrnrlon=70,urcrnrlat=13,urcrnrlon=74.5,resolution='f')
mp.drawcoastlines()
mp.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)
parallels = np.arange(0.,81,1.)
meridians = np.arange(10.,351.,1.)
mp.drawparallels(parallels,labels=[True,False,False,False])
mp.drawmeridians(meridians,labels=[False,False,False,True])
mp.scatter(lons,lats,latlon=True,s=100,c=months,marker='.',cmap="summer")
cbar=mp.colorbar()
cbar.set_label('deployed month')
#annotating all points
#for i in range(len(lons)):
    #x,y=mp(lons[i],lats[i])
    #plt.text(x,y,str(data.variables['PLATFORM_NUMBER']))
plt.title('FLOAT LOCATIONS-2017_Oct_Nov_Lakshadweep')
plt.figure(figsize=(20,20))

df=pd.DataFrame({'date':dates,'float_id':float_id,'latitude':lats,'longitude':lons})
df.to_csv('float_id_data.csv')
plt.show()