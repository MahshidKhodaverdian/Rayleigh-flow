#Mahshid khodaverdian-Mohammad amin eslami
#Rayleigh Flow
from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
gama = 1.4
# np.linspace = range of mach 
mach = np.linspace(0.01,5,500)
g = gama + 1
# P = p/pstar
P = ((g) / (1 + ((gama ) * np.power(mach , 2))))
# T = t/tstar
T = (np.power(mach , 2) * (np.power(g , 2)) / np.power((1 + ((gama ) * np.power(mach , 2))) , 2))
# RHO/RHOstar=RHO
RHO = ((1 + ((gama ) * np.power(mach , 2))) / (np.power(mach , 2) * g))
# Tstar = T0/T0star
Tstar = (((np.power(mach , 2) * g) * 2) / np.power((1 + ((gama ) * np.power(mach , 2))) , 2)) * (1 + (((gama - 1) / 2) * np.power(mach , 2)))
# Pstar= p0/p0star
Pstar = np.power(((1 + (((gama - 1) / 2) * np.power(mach , 2))) / (g / 2)) , (gama / (gama - 1))) * (g / (1 + ((gama ) * np.power(mach , 2))))
Rayleigh = {'M':mach, 'P/Pstar':P, 'T/Tstar':T, 'RHO/RHOstar':RHO, 'T0/T0star':Tstar, 'P0/P0star':Pstar}
TableOfRayleigh = pd.DataFrame(Rayleigh)
TableOfRayleighPlot = pd.DataFrame(Rayleigh, index=mach)
TableOfRayleighPlot[['P/Pstar', 'T/Tstar', 'RHO/RHOstar', 'T0/T0star', 'P0/P0star']].plot()
display(TableOfRayleigh)
plt.xlim(0,5)
plt.ylim(-0.5,10)
plt.title('Rayleigh-Flow')
plt.xlabel('Mach')
plt.ylabel('properties')
plt.grid()
plt.show()