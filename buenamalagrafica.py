import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

plt.rcParams['font.family'] = 'Times New Roman'

## Datos
mean = 0
stdev = 1

def function(x):
    return x

N = 10
x = np.linspace(0, 30, N)
y = np.copy(function(x))

for k in range(len(y)):
    y[k] += random.gauss(mean, stdev)

error_x = 1 * np.ones(N)
error_y = 2 * np.ones(N)

## Mala gráfica
plt.figure()
plt.plot(x, y, '-o')
plt.xlabel('Tiempo (s)', fontsize=5)
plt.ylabel('Voltaje (V)', fontsize=5)
plt.xlim(-20, 60)
plt.ylim(-30, 60)
plt.savefig('assets/fig/malagrafica.png')

## Buena gráfica
plt.figure()
plt.plot(x, x, '-', label='Ajuste', color='black')
plt.errorbar(x, y, fmt='s', xerr=error_x, yerr=error_y, label='Experimental', capsize=2, elinewidth=0.5)
plt.xlabel('Tiempo (s)', fontsize=15)
plt.ylabel('Voltaje (V)', fontsize=15)
plt.tick_params(axis='both', which='both', labelsize=15)
plt.legend()
plt.savefig('assets/fig/buenagrafica.png')