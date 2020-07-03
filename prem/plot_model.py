#!/Users/marcoquiroz/anaconda3/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv('PREM_1s.csv', names=['Radius','Depth','Density','Vpv','Vph','Vsv','Vsh','eta','Q-mu','Q-kappa'])

# Preview the first 5 lines of the loaded data
print(data.Depth)#data.head())

plt.plot(data.Vpv,data.Depth,'b', clip_on=False,label='V$_{p}$')
plt.plot(data.Vsv,data.Depth,'r', clip_on=False,label='V$_{s}$')
plt.xlim(0,14)
plt.ylim(0,data.Depth.max())
plt.gca().invert_yaxis()
plt.ylabel('Depth (km)')
plt.xlabel('Velocity (km/s)')
plt.title('PREM Velocity Model')
plt.legend()
plt.grid(color='lightgray', linestyle='--', linewidth=0.25)
plt.yticks(np.arange(0,6000+500,500))
plt.gca().set_aspect(0.0045)
plt.show()
