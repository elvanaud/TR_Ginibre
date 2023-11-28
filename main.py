import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

print("Vizualization of Ginibre eigenvalues and Saturn effect")

N = 3000
mu = 0.0
sigma = 1.0/np.sqrt(2*N)

gen = rd.default_rng()
mat = gen.normal(mu,sigma, (N,N))+gen.normal(mu,sigma,(N,N))*complex(0,1)
print(mat)

eigenvalues, _= np.linalg.eig(mat)
print(eigenvalues)


#plt.xlim(-1.0,1.0)
#plt.ylim(-1.0,1.0)
plt.gca().set_aspect('equal')
plt.scatter(eigenvalues.real, eigenvalues.imag, s = 2,c="red")
plt.title("Eigenvalues of Ginibre matrix")
plt.show()