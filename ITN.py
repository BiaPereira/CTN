import os
import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from PIL import Image, ImageDraw
import ezodf

#Opens file
#filename = input('Name of the file: ')
file = open('F2LiCl_001.txt')
print("open")
fileR = file.read()
#print (fileR)
print (type(fileR))


g = fileR.split(' ',-1)
print(g)
leng = len(g)
print (leng)

i=0
x = []
y = []
for i in range(0,leng-1,4):

    print ('Novos valores')
    print(g[i + 1])
    print(g[i+3])
    x.append(float(g[i + 1]))
    y.append(float(g[i+3]))

print(x)
print('Maximo de x', max(x))

print('Maximo de y', max(y))
print (y)

plt.plot(x,y)
plt.grid()
plt.show()
print ('fim')

