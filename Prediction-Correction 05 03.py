import numpy as np
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


def PredCorr(A, n, epsilon, tolContour, pas):
    global Z
    #trouver le premier point z1 par la methode de Newton
    lambda0 = np.linalg.eig(A)[0][0]
    theta = epsilon
    d = 1j
    z = lambda0 + d*theta
    U, S, V = g(z, A, n)
    while(np.abs((S[n-1] - epsilon)) / epsilon > 0.001):
        z = z - (S[n-1] - epsilon)*d / ((-d*np.vdot(V[n-1], U[n-1])).real)
        U, S, V = g(z, A, n)
        #newton iterate 
    Z = np.append(Z, z)
    
    #on trouve le point suivant
    rk = d*(np.vdot(V[n-1], U[n-1]) / np.abs(np.vdot(V[n-1], U[n-1])))
    zkPred = z + pas*rk
    Uk, Sk, Vk = g(zkPred, A, n)
    zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[n-1], Vk[n-1]))
    
    #puis tous les points suivants tant que l'on est pas revenu a z1
    while(np.abs((zk - z)) > tolContour):
        Z = np.append(Z, zk)
        rk = d*(np.vdot(Vk[n-1], Uk[n-1]) / np.abs(np.vdot(Vk[n-1], Uk[n-1])))
        zkPred = zk + pas*rk
        Uk, Sk, Vk = g(zkPred, A, n)
        zk = zkPred - (Sk[n-1] - epsilon) /(np.vdot(Uk[n-1], Vk[n-1]))

PredCorr(creerMat(10) , 10, 0.1, 0.1, 0.1)

C = 0.1
X = [z.real for z in Z]
Y = [z.imag for z in Z]
#plt.contour(X, Y, 1, levels = [1])
plt.plot(Z)
plt.xlabel('Reels')
plt.ylabel('Imaginaires')
plt.title('Contour du pseudo-spectre')
plt.grid(True)
plt.show()
