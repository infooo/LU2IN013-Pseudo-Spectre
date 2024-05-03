import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
Z = np.array([], dtype=np.float64)
def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def g(z, A, n):
    U, S, V = np.linalg.svd(np.identity(n)*z-A)
    V = V.conjugate().T
    return U, S, V

def h(z, theta, A, n, epsilon):
    return g(z + 1j*theta, A, n)[1][n-1] - epsilon


def PredCorr(A, n, epsilon, tolContour, pas, nbPoints):
    global Z
    #trouver le premier point z1 par la methode de Newton
    lambda0 = np.linalg.eig(A)[0][0]
    theta = epsilon
    d = 1j
    z = lambda0 + d*theta
    U, S, V = g(z, A, n)
    while(np.abs((S[n-1] - epsilon)) / epsilon > 0.01):
        print((S[n-1] - epsilon)/epsilon)
        print("PREMIER POINT")
        z = z - (S[n-1] - epsilon)*d / ((-d*np.vdot(V[n-1], U[n-1])).real)
        U, S, V = g(z, A, n)
        #newton iterate 
    Z = np.append(Z, z)
    
    rk = d*(np.vdot(V[n-1], U[n-1]) / np.abs(np.vdot(V[n-1], U[n-1])))
    zkPred = z + pas*rk
    Uk, Sk, Vk = g(zkPred, A, n)
    zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[n-1], Vk[n-1]))
    Z = np.append(Z, zk)
    
    #puis tous les points suivants tant que l'on est pas revenu a z1
    for k in range(1, nbPoints):
        print(np.abs((zk - z)))
        rk = d*(np.vdot(Vk[n-1], Uk[n-1]) / np.abs(np.vdot(Vk[n-1], Uk[n-1])))
        zkPred = zk + pas*rk
        Uk, Sk, Vk = g(zkPred, A, n)
        zk = zkPred - (Sk[n-1] - epsilon) /(np.vdot(Uk[n-1], Vk[n-1]))
        Z = np.append(Z, zk)
    print("FIN C FINI")

PredCorr(creerMat(10) , 10, 0.1, 0.1, 0.1, 1000)

Z_real = [z.real for z in Z]
Z_imag = [z.imag for z in Z]

# Plot real vs imaginary parts
plt.plot(Z_real, Z_imag, 'bo')  # 'bo' for blue circles
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Complex numbers in Z')
plt.grid(True)
plt.show()