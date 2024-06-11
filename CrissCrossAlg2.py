import numpy as np
import PredictionCorrection
import matplotlib.pyplot as plt
import math

#Algo Criss-Cross pour l'abscisse du pseudospectre (sup Re z, z dans le pseudospectre)

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def svmin(A, n, x, y):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def rightmostVap(A):
    vaps = np.linalg.eig(A)[0]
    rmVap = max(vaps, key = lambda x: x.real)
    return rmVap 

def ValeurSinguliereHorizontale(A, n, y, epsilon, tol):
    matAugmentee = np.block([
        [-y * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), 1j*A + y * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    maxvap = max([x.imag for x in vaps if x.real == 0])
    return maxvap

def ValeurSinguliereVerticale(A, n, x, epsilon, tol):
    Y = np.array([], dtype=np.float64)
    matAugmentee = np.block([
        [x * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), A - x * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    for vap in vaps:
        if vap.real == 0:
            if np.abs(svmin(A, n, x, vap.imag) - epsilon) < tol:
                Y = np.append(Y, vap.imag)
    return Y


def CrissCrossAbscisse(A, n, epsilon, nbPoints, tol):
    z1 = rightmostVap(A)

    #etape 2
    x = z1.real
    i = 0 
    midpoints = np.array([x], dtype=np.float64)
    X = np.array([], dtype=np.float64)
    while i < 10: 

        for x in midpoints:
            X = np.append(X, ValeurSinguliereHorizontale(A, n, z1.imag, epsilon, tol))
        nvx = X[0]
        nvy = Y[0]
        for j in range(len(X)):
            if X[j] > nvx:
                nvx = X[j]
                nvy = Y[j]

        z1 = nvx + 1j*nvy.imag
        zk = z1
        
        Y = np.array([zk.imag], dtype=np.float64)

        #etape 3: intersections verticales basses
        
        Y = np.append(Y , ValeurSinguliereVerticale(A, n, zk.real, y, epsilon, tol))
        Y.sort()
        zk = z1

        l = len(Y)
        
        while(2*i+1 < l):
            midpoints = np.append(midpoints, (y[2*i] + y[2*i + 1]) / 2)
        i += 1
            
A = creerMat(10)
fig, ax = plt.subplots()
PredictionCorrection.PredCorr(ax, A, 10, 0.01, 0.0001, 0.005)

        