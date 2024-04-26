import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math

U = []
V = []
S = []

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def g(z, A, n):
    U, S, V = np.linalg.svd(np.identity(n)*z-A)
    return U, S, V

def h(z, theta, A, n, epsilon):
    return g(z + 1j*theta, A, n)[1][n-1] - epsilon


def fp(n):
    global U, V 
    return (np.vdot(V[n-1], U[n-1]))

def PredCorr(A, n, epsilon, tolContour, pas):
    global U, S, V
    #trouver le premier point z1 par la methode de Newton
    lambda0 = np.linalg.eig(A)[0][0]
    theta = 0
    z1 = sp.optimize.newton(h, lambda0, fprime = fp, args = (lambda0, theta, A, n, epsilon), tol = 10**(-18), maxiter = 200)
    U, S, V = g(z1, A, n)

    #on trouve le point suivant
    rk = 1j*(np.vdot(V1[n-1], U1[n-1]) / np.abs(np.vdot(V1[n-1], U1[n-1])))
    zkPred = z1 + pas*rk
    Uk, Sk, Vk = g(zkPred, A, n)
    zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[n-1], Vk[n-1]))
    #puis tous les points suivants tant que l'on est pas revenu a z1
    while(sp.spatial.distance.cdist(zk, z1) > tolContour):
        rk = 1j*(np.vdot(Vk[n-1], Uk[n-1]) / np.abs(np.vdot(Vk[n-1], Uk[n-1])))
        zkPred = zk + pas*rk
        Uk, Sk, Vk = g(zkPred, A, n)
        zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[n-1], Vk[n-1]))