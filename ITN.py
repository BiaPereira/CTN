import os
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
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

lim_min=int(input('Lower limit: '))
lim_max=int(input('Upper limit: ' ))

def zoom_gráfico (minimo, maximo):
    lmin = x.index(minimo)
    lmax = x.index(maximo)
    new_x = []
    new_y = []
    new_x = x[lmin:lmax + 1]
    new_y = y[lmin:lmax + 1]

    plt.plot(new_x, new_y)
    plt.yscale('log', nonposy='clip')
    plt.ylabel('Intensidade')
    plt.xlabel('Canal')
    plt.show()



zoom_gráfico(lim_min,lim_max)
resp = input('Gráfico Correto? Sim/Não: ')
while resp == 'Não':
    lim_min = int(input('Lower limit: '))
    lim_max = int(input('Upper limit: '))
    zoom_gráfico(lim_min,lim_max)
    resp = input('Gráfico Correto? Sim/Não: ')

#print ('entre que valores está o pico máximo1?')
    #min1 = int(input('Lower limit: '))
    #max1 = int(input('Upper limit: '))
min1 = 2620
max1 = 2750
xx = x[min1:max1 + 1]
yy = y[min1:max1 + 1]
print (xx)
print ('veotr yy',yy)
maxy = max(yy)
print ('maxy',maxy)
FWHMy = maxy/2
print ('FWHMy',FWHMy)
print ('yy.index(maxy)',yy.index(maxy))
print ('yy.index(FWHMy)', yy.index(FWHMy))

index_max_y = yy.index(maxy) + min1
index_FWHM_y = yy.index(FWHMy) + min1

FWHMx = (abs(index_max_y-index_FWHM_y)*2)
FWHM2 = (abs(index_max_y-index_FWHM_y))

print ('FWHMX' ,FWHMx)
print ('index_max_y',index_max_y)
print ('index_FWHM_y',index_FWHM_y)

inicio = index_max_y - min1 - FWHM2
print(type(inicio))
fim = inicio + FWHMx
print(type(fim))
area = 0
j = inicio
print (inicio)
print (fim)
for j in range(inicio, fim,1):
    print (j)
    area = (area + yy[j])
    print ('area:', area)

xx=np.array(xx, dtype=float)

def gaussiana (A, y0,index_x, FWHM, x):
    gauss = y0 + (A/((FWHM/(np.log(4))**(1/2))))*np.exp(-2*((x-index_x)**2)/((FWHM/(np.log(4))**(1/2))**2))
    return gauss
print (gaussiana(area, 10,yy.index(maxy), FWHMx, xx))
k = gaussiana(area, 10,index_max_y, FWHMx, xx)
print (type (k))
print (type (xx))
print (xx)
plt.plot(xx,k, xx,yy)

plt.show()
plt.savefig

