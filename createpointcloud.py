import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np
import random
from mpl_toolkits.mplot3d import axes3d


plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.serif'] = 'Ubuntu' 
plt.rcParams['font.monospace'] = 'Ubuntu Mono' 
plt.rcParams['font.size'] = 14 
plt.rcParams['axes.labelsize'] = 12 
plt.rcParams['axes.labelweight'] = 'bold' 
plt.rcParams['axes.titlesize'] = 12 
plt.rcParams['xtick.labelsize'] = 12 
plt.rcParams['ytick.labelsize'] = 12 
plt.rcParams['legend.fontsize'] = 12 
plt.rcParams['figure.titlesize'] = 12 
plt.rcParams['image.cmap'] = 'jet' 
plt.rcParams['image.interpolation'] = 'none' 
plt.rcParams['figure.figsize'] = (12, 10) 
plt.rcParams['axes.grid']=True
plt.rcParams['lines.linewidth'] = 2 
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']

x = []
y = []
z = []
for i in range(2000):
    u = np.random.normal(0,1)
    v = np.random.normal(0,1)
    w = np.random.normal(0,1)
    norm = (u*u + v*v + w*w)**(0.5)
    xi,yi,zi = u/norm,v/norm,w/norm
    x.append(xi)
    y.append(yi)
    z.append(zi)
fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d'})
# ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
ax.scatter(x, y, z, s=100, c='r', zorder=10)
ax.set_title('Example of a uniformly sampled sphere', fontdict={'fontsize':20})
fig = plt.figure(figsize=plt.figaspect(0.5))
plt.show()

