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
    np.matrix.H(V)
    return U, S, V

def h(z, theta, A, n, epsilon):
    return g(z + 1j*theta, A, n)[1][n-1] - epsilon


def PredCorr(A, n, epsilon, tolContour, pas):
    global Z
    #trouver le premier point z1 par la methode de Newton
    lambda0 = np.linalg.eig(A)[0][0]
    theta = epsilon
    z1 = lambda0 + 1j*theta
    print(lambda0)
    U1, S1, V1 = g(z1, A, n)
    while(np.abs((S1[n-1] - epsilon)/epsilon)>0.001):
        print(z1)
        U1, S1, V1 = g(z1, A, n)
        z1 = z1 - (S1[n-1] - epsilon)*1j /((-1j*np.vdot(V1[n-1], U1[n-1])).real)
        #newton iterate 
    
    #on trouve le point suivant
    rk = 1j*(np.vdot(V1[n-1], U1[n-1]) / np.abs(np.vdot(V1[n-1], U1[n-1])))
    zkPred = z1 + pas*rk
    Uk, Sk, Vk = g(zkPred, A, n)
    zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[n-1], Vk[n-1]))
    
    #puis tous les points suivants tant que l'on est pas revenu a z1
    while(np.abs((zk - z1)) > tolContour):
        print("z")
        Z = np.append(Z, zk)
        rk = 1j*(np.vdot(Vk[n-1], Uk[n-1]) / np.abs(np.vdot(Vk[n-1], Uk[n-1])))
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
