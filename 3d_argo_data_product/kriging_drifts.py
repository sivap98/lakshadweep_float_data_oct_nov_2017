# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:05:31 2021

@author: Dell
"""

from pykrige.uk3d import UniversalKriging3D
from pykrige.ok3d import OrdinaryKriging3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:/myi/lakshadweep/lakshadweep_data_oct_nov17.csv')
x=np.array(df['latitude'])
y=np.array(df['longitude'])
z=np.array(df['Sea Pressure in decibar'])
val=np.array(df['sea temperature in deg_celcius'])
gridx=np.linspace(9,11,num=12,endpoint=True)
gridy=np.linspace(70.6,73,num=12,endpoint=True)
gridz=np.linspace(2,101,num=20,endpoint=True)
ok3d=OrdinaryKriging3D(x,y,z,val,variogram_model='linear')
k3d1,ss3d=ok3d.execute('grid',gridx,gridy,gridz)
uk3d=UniversalKriging3D(x,y,z,val,variogram_model='linear',drift_terms=["regional_linear"])
k3d2,ss3d=uk3d.execute('grid',gridx,gridy,gridz)
zg,yg,xg=np.meshgrid(gridz,gridy,gridx,indexing='ij')
uk3d=UniversalKriging3D(x,y,z,val,variogram_model='linear',drift_terms=["specified"],
specified_drift=[x,y,z])
k3d3, ss3d = uk3d.execute(
"grid", gridx, gridy, gridz, specified_drift_arrays=[xg, yg, zg]
)
func = lambda x, y, z: x
uk3d = UniversalKriging3D(
x,
y,
z,
val,
variogram_model="linear",
drift_terms=["functional"],
functional_drift=[func],
)
k3d4, ss3d = uk3d.execute("grid", gridx, gridy, gridz)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.imshow(k3d1[:, :, 0], origin="lower")
ax1.set_title("ordinary kriging")
ax2.imshow(k3d2[:, :, 0], origin="lower")
ax2.set_title("regional lin. drift")
ax3.imshow(k3d3[:, :, 0], origin="lower")
ax3.set_title("specified drift")
ax4.imshow(k3d4[:, :, 0], origin="lower")
ax4.set_title("functional drift")
plt.tight_layout()
plt.show()
#fig3d=plt.figure(figsize=(5,5))
#plot3d=fig3d.add_subplot(111,projection='3d')
#plot3d.scatter(xg,yg,zg)
#plt.show()

