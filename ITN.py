import os
import numpy as np
import matplotlib.pyplot as plt
from bisect import bisect
from lmfit.models import GaussianModel, ConstantModel
from scipy.odr import *
from lmfit import Model

greek_alphabet = {u'\u03A7'}

#Opens file
filename = input('Name of the file: ')
#filename = 'F2LiCl_001.txt'
tam = len(filename)

if filename[tam-3:tam] == 'txt':
    file = open(filename)
if filename[tam-3:tam] == 'odf':
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + ".txt")
    file = open (filename[0:tam-3]+'txt')
fileR = file.read()

def grafico (x,y):
    # legend
    plt.plot(x, y, label="Experimental")
    plt.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)
    plt.yscale('log', nonposy='clip')
    plt.ylabel('Intensidade')
    plt.xlabel('Canal')
    print('3')
    print(x)
    print (y)
    plt.show()


#function
def zoom_gráfico (minimo, maximo):
    lmin = x.index(minimo)
    print('1')
    lmax = x.index(maximo)
    new_x = []
    new_y = []
    print('2')
    new_x = x[lmin:lmax + 1]
    new_y = y[lmin:lmax + 1]
    print('m')
    print (new_x)
    print(new_y)
    grafico(new_x, new_y)

#Gauss + line + bimodal

def gaussian (x, A,index_x, FWHM):
    gauss = (A/((FWHM/(np.log(4))**(1/2))))*np.exp(-2*((x-index_x)**2)/((FWHM/(np.log(4))**(1/2))**2))
    return gauss

def line (x, m, b):
    return m*x+b

def bimodal(x,A1,index1,FWHM1,A2,index2,FWHM2):
    return gaussian(x,A1,index1,FWHM1)+gaussian(x,A2,index2,FWHM2)

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
print (min_x)
max_y = max(y)
min_y = min(y)
print (len(x))
print (len(y))

# Plot
plt.grid()
grafico(x,y)


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

print ('Entre que valores está o pico2 máximo?')
min_xx = int(input('Lower limit: '))
max_xx = int(input('Upper limit: '))
print ('segundo pico')
min_xx2 = int(input('Lower limit: '))
max_xx2 = int(input('Upper limit: '))
y0 = int(input('y0:'))
#min_xx = 2530
#max_xx = 2640
#min_xx2 = 2630
#max_xx2 = 2740

if min_xx<min_xx2:
    print('1')
    xtotal = x[min_xx:max_xx2 + 1]
    ytotal= y[min_xx:max_xx2 + 1]
if min_xx>min_xx2:
    print('2')
    xtotal = x[min_xx2:max_xx + 1]
    ytotal = y[min_xx2:max_xx + 1]

# New vector x and y (shorter)
xx = x[min_xx:max_xx + 1]
yy = y[min_xx :max_xx + 1]

xx2 =x[min_xx2:max_xx2 + 1]
yy2 = y[min_xx2:max_xx2 + 1]

grafico(xtotal,ytotal)

#Obter os valores
max_yy = max(yy)#max_counts
FWHMyy = max_yy/2 #number of FWHM yy
#print ('FWHMyy',FWHMyy)

#In case that FWHM does not appear in yy
if FWHMyy in yy:
    index_FWHM_y = yy.index(FWHMyy) + min_xx

else:
    y2 = sorted(yy) #order
    #print (y2)
    index_FWHM_y2 = bisect(y2,FWHMyy)
    #print ('index_FWHM_y2',index_FWHM_y2)
    number = y2[index_FWHM_y2]
    #print (number)
    index_FWHM_y = yy.index(number) + min_xx

max_yy2 = max(yy2)#max_counts
FWHMyy2 = max_yy2/2 #number of FWHM yy

if FWHMyy2 in yy2:
    index_FWHM_y2 = yy2.index(FWHMyy2) + min_xx2

else:
    y2 = sorted(yy2) #order
    #print (y2)
    index_FWHM_y2 = bisect(y2,FWHMyy2)
    #print ('index_FWHM_y2',index_FWHM_y2)
    number = y2[index_FWHM_y2]
    #print (number)
    index_FWHM_y2 = yy2.index(number) + min_xx2



#print ('yy.index(maxy)',yy.index(max_yy))
#print ('yy.index(FWHMy)', index_FWHM_y)
index_max_y = yy.index(max_yy) + min_xx
index_max_y2 = yy2.index(max_yy2) + min_xx2

FWHM_xx = (abs(index_max_y-index_FWHM_y)*2)
#print ('FWHM', FWHM_xx)
FWHM2 = (abs(index_max_y-index_FWHM_y))

FWHM_xx2 = (abs(index_max_y2-index_FWHM_y2)*2)
FWHM22 = (abs(index_max_y2-index_FWHM_y2))

#Area
inicio = index_max_y - min_xx - FWHM2
fim = inicio + FWHM2
#print(yy)
# print (inicio)
#print (fim)
area = 0
j = inicio
for j in range(inicio, fim,1):
    area = (area + yy[j])
    #print ('area1:', area)

inicio2 = index_max_y2 - min_xx2 - FWHM22
fim2 = inicio2 + FWHM_xx2
area2 = 0
g = inicio2
for g in range(inicio2, fim2,1):
    area2 = (area2 + yy2[g])
   # print ('area2:', area2)

xx=np.array(xx, dtype=float)
yy=np.array(yy, dtype=float)
xx2=np.array(xx2, dtype=float)
yy2=np.array(yy2, dtype=float)
xtotal=np.array(xtotal, dtype=float)
ytotal=np.array(ytotal, dtype=float)

mod = Model(bimodal) + Model(line)
#plt.plot(bimodal(x=xtotal, A1= area, index1=index_max_y, FWHM1=FWHMyy,A2 = area2, index2= index_max_y2, FWHM2= FWHMyy2))
pars = mod.make_params(A1= area, index1=index_max_y, FWHM1=FWHMyy,A2 = area2, index2= index_max_y2, FWHM2= FWHMyy2, m=0, b=10)
pars['FWHM1'].min > 0.001         # sigma  > 0
pars['FWHM2'].min > 0.001     # amplitude > 0


resul = mod.fit(ytotal, pars, x=xtotal, weights=1/np.sqrt(ytotal))

print(resul.fit_report())
t=resul.fit_report().split('\n',-1)
print (t)
l = t[7]
tamanho = len(l)
valorchi = l[24:tamanho]

#for w in range (11, 17, 1):
 #   valor =[]
  #  incer = []
   # val= t[w]
    #slp=val.split(' ', -1)
    #print (slp)
    #num = (map(lambda x: float(x), t[11]))
    #valor = valor + num
# incer = incer + float(val [13])
#     print ('dd', valor)
#   print(incer)
#   #num = float (val)
    #new = np.append(num)
    #print (new)

#apro =np.around(num, decimals=1)
#print(type(valorchi))
#print('aa', apro)


plt.plot(xtotal, ytotal,         'b+', label="Experimental")
plt.plot(xtotal, resul.init_fit, 'k--', color = 'grey' ,label="Initial Fit")
plt.plot(xtotal, resul.best_fit, 'r-', color = "green",label="Best Fit")
plt.yscale('log', nonposy='clip')
plt.ylabel('Intensidade')
plt.xlabel('Canal')
plt.figtext(.165, 0.806, r'$\chi$')
plt.figtext(.18, 0.8, '='+valorchi)
plt.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)
plt.show()

# File
newfile = input('file name:')

if os.path.exists(newfile):
    y = open(newfile, 'a')
    y.write('\n')
    y.write("\n".join(map(lambda x: str(x), t[11:17])))
    y.close()
else:
    f = open(newfile, 'w')
    f.write("\n".join(map(lambda x: str(x), t[11:17])))
    f.close()

#print ('\n')
#print ('New Plot')

#PS= FWHMyy/2*(np.log(4))**(1/2)
#print('area', area)

#model = GaussianModel(prefix='peak_') + ConstantModel()
#params = model.make_params(c=y0, peak_center=index_max_y, peak_sigma=PS, peak_amplitude= area)

#result = model.fit(yy, params, x=xx,  weights= 1/np.sqrt(yy))
#print(result.fit_report())
#plt.plot(xx, yy, 'b+', color = 'blue')
#plt.plot(xx, result.best_fit, color = 'orange')
#plt.show()