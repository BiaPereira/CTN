import os
import numpy as np

#Opens file
filename = input('Name of the file: ')
file = open(filename)
print('\n')
fileR = file.read()
print(fileR)
print