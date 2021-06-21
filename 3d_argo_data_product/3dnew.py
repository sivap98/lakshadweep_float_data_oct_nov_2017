# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:24:33 2021

@author: Dell
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df=pd.read_csv('D:/myi/lakshadweep/lakshadweep_data_oct_nov17.csv')
x=np.linspace(9,11,num=20,endpoint=True)
y=np.linspace(70.6,73,num=20,endpoint=True)
z=np.linspace(2,102,num=20,endpoint=True)
#t=np.array(datetime.time(df['date']))
#val=np.array(df['sea temperature in deg_celcius'])
reg=linear_model.LinearRegression()
reg.fit(df[['latitude','longitude','Sea Pressure in decibar']],df['sea temperature in deg_celcius'])

X,Y,Z=np.meshgrid(x,y,z)
val=-0.26606282*X-1.09018624*Y-0.14194047*Z
def f(X, Y,Z):
    return -0.26606282*X-1.09018624*Y-0.14194047*Z+111.6282071803545#reg.coef_ and reg.intercept_

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
p=ax.scatter3D(X,Y,Z,c=f(X,Y,Z),cmap="jet")

ax.set_xlabel('latitude')
ax.set_ylabel('longitude')
ax.set_zlabel('pressure')
plt.colorbar(p,location="left",label="TEMP")
plt.gca().invert_zaxis()
plt.show()
plt.tight_layout()
ax.view_init(5,15)
