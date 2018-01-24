import os
import numpy as np
import matplotlib.pyplot as plt
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
#f = fileR.split('\n', -1)
#print (f)
leng = len(g)
print (leng)
#print (shape)
#print(g)
i=0
x = []
y = []
for i in range(0,leng-1,4):

    print ('Novos valores')
    print(g[i + 1])
    print(g[i+3])
    x.append(g[i + 1])
    y.append(g[i+3])
print (x)
maxx = max(x)
print (len(x))
print (y)
maxy = max(y)
print (len(y))
print (type(x))

plt.plot(x,y)
#plt.axis([0, 160, 0, 0.03])
plt.show()

