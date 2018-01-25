import os
import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from PIL import Image, ImageDraw
import ezodf
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes


#Opens file
#filename = input('Name of the file: ')
file = open('F2LiCl_001.txt')
fileR = file.read()
#print (fileR)


g = fileR.split(' ',-1)
leng = len(g)

#Two list
i=0
x = []
y = []
for i in range(0,leng-1,4):

    x.append(float(g[i + 1]))
    y.append(float(g[i+3]))

print('Maximo de x', max(x))
print('Maximo de y', max(y))


# Plot
plt.plot(x,y)
plt.grid()

# legend
plt.plot(y, label="Experimental")
#plt.plot(gauss, label="Gaussiana") # legenda para a gaussiana
plt.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)

# Axes
plt.ylabel('Intensidade')
plt.xlabel('Canal')
#plt.axhline(y=0) linha horizontal
#plt.axvline(x=0) linha vertical
plt.yscale('log', nonposy='clip')
plt.show()

#lim_min=int(input('Lower limit: '))
#lim_max=int(input('Upper limit: ' ))
lim_min = 2000
lim_max = 3000

lmin = x.index(lim_min)
lmax = x.index(lim_max)
new_x = []
new_y = []
new_x = x[lmin:lmax+1]
new_y = y[lmin:lmax+1]


plt.plot(new_x,new_y)
plt.yscale('log', nonposy='clip')
plt.ylabel('Intensidade')
plt.xlabel('Canal')

plt.show()
