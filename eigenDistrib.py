import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp

def expSeries(n, z):
    zPowK=1.0
    res= 0.0
    factK = 1
    for k in range(n+1):
        res+= zPowK/factK
        zPowK*=z
        factK*=(k+1)
    return res


def rho(N,x,y):
    return np.sqrt(2.0/np.pi)*y*np.exp(y**2-x**2)*sp.special.erfc(np.sqrt(2)*y)*expSeries(N-2, x**2+y**2)
    
y, x = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
z = rho(16,x,y)
#print(z)

z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolormesh')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)

plt.show()