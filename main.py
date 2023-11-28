import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

print("Vizualization of Ginibre eigenvalues and Saturn effect")
gen = rd.default_rng()
N = 16
mu = 0.0
sigma = 1.0/np.sqrt(1*N)

def obtainGinibreEig(N,mu,sigma):
    mat = gen.normal(mu,sigma, (N,N)) #+gen.normal(mu,sigma,(N,N))*complex(0,1)
    #print(mat)

    eigenvalues, _= np.linalg.eig(mat)
    #print(eigenvalues)


    #plt.xlim(-1.0,1.0)
    #plt.ylim(-1.0,1.0)
    return eigenvalues

eigenvalues = []
for _ in range(1000):
    eigenvalues.append(obtainGinibreEig(N,mu,1.0))
    
print(eigenvalues)
values = np.append([], eigenvalues)
print(values)

plt.gca().set_aspect('equal')
plt.scatter(values.real, values.imag, s = 1,c="red")
plt.title("Eigenvalues of Ginibre matrix")
plt.show()
