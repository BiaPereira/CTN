import os
import numpy as np
import matplotlib.pyplot as plt
from bisect import bisect
from matplotlib.backends.backend_pdf import PdfPages
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
filename = input('Name of the file: ')
tam = len(filename)
if filename[tam-3:tam] == 'txt' :
    file = open(filename)
if filename[tam-3:tam] == 'odf' :
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".txt")
    file = open(filename)
else:
    print('Ficheiro não suportado')


fileR = file.read()

#function
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

#Gauss
def gaussiana (A, y0,index_x, FWHM, x):
    gauss = y0 + (A/((FWHM/(np.log(4))**(1/2))))*np.exp(-2*((x-index_x)**2)/((FWHM/(np.log(4))**(1/2))**2))
    return gauss

#split
g = fileR.split(' ',-1)
leng = len(g)

#Two list
i=0
x = []
y = []
for i in range(0,leng-1,4):

    x.append(float(g[i + 1]))
    y.append(float(g[i+3]))

#Max and min vector x and y
max_x = max(x)
min_x = min(x)
max_y = max(y)
min_y = min(y)
print('Maximo de x', max_x)
print('Maximo de y', max_y)


# Plot
plt.plot(x,y)
plt.grid()

# legend
plt.plot(y, label="Experimental")
plt.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)

# Axes
plt.ylabel('Intensidade')
plt.xlabel('Canal')
plt.xlim(min_x,max_x)
#plt.ylim(min_y,max_y)
#plt.axhline(y=0) linha horizontal
#plt.axvline(x=0) linha vertical
plt.yscale('log', nonposy='clip')
plt.show()


#---------------------New plot


# input limit plot
lim_min=int(input('Lower limit: '))
lim_max=int(input('Upper limit: ' ))

zoom_gráfico(lim_min,lim_max)
resp = input('Gráfico Correto? Sim/Não: ')
while resp == 'Não':
    lim_min = int(input('Lower limit: '))
    lim_max = int(input('Upper limit: '))
    zoom_gráfico(lim_min,lim_max)
    resp = input('Gráfico Correto? Sim/Não: ')

print ('Entre que valores está o pico máximo1?')
min_xx = int(input('Lower limit: '))
max_xx = int(input('Upper limit: '))

# New vector x and y (shorter)
xx = x[min_xx:max_xx + 1]
yy = y[min_xx :max_xx + 1]


max_yy = max(yy)#max_counts
FWHMyy = max_yy/2 #number of FWHM yy
print ('FWHMyy',FWHMyy)

#In case that FWHM does not appear in yy
if FWHMyy in yy:
    index_FWHM_y = yy.index(FWHMyy) + min_xx

else:
    y2 = sorted(yy) #order
    print (y2)
    index_FWHM_y2 = bisect(y2,FWHMyy)
    print ('index_FWHM_y2',index_FWHM_y2)
    number = y2[index_FWHM_y2]
    print (number)
    index_FWHM_y = yy.index(number) + min_xx

print ('yy.index(maxy)',yy.index(max_yy))
print ('yy.index(FWHMy)', index_FWHM_y)
index_max_y = yy.index(max_yy) + min_xx

FWHM_xx = (abs(index_max_y-index_FWHM_y)*2)
FWHM2 = (abs(index_max_y-index_FWHM_y))

print ('FWHMX' ,FWHM_xx)
print ('index_max_y',index_max_y)
print ('index_FWHM_y',index_FWHM_y)

#Area
inicio = index_max_y - min_xx - FWHM2
print(type(inicio))
fim = inicio + FWHM_xx
print(type(fim))
area = 0
j = inicio
print ('inicio',inicio)
print ('fim', fim)
for j in range(inicio, fim,1):
    print (j)
    area = (area + yy[j])
    #print ('area:', area)

xx=np.array(xx, dtype=float)

#print (gaussiana(area, 10,yy.index(max_yy), FWHM_xx, xx))

# New plot
k = gaussiana(area, 10,index_max_y, FWHM_xx, xx)
plt.plot(xx,k, xx,yy)
plt.show()
