import numpy as np
import matplotlib.pyplot as plt
import math

#Algo Criss-Cross pour l'abscisse du pseudospectre (sup Re z, z dans le pseudospectre)
Y = np.array([], dtype=np.float64)

def svmin(A, n, x, y):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def rightmostVap(A):
    vaps = np.linalg.eig(A)[0]
    rmVap = max(vaps, key = lambda x: x.real)
    return rmVap 

def estValeurSinguliereHorizontale(A, n, x, y, epsilon, tol):
    matAugmentee = np.block([
        [-y * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), 1j*A + y * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    for vap in vaps:
        if np.abs(vap - 1j*x) < tol:
            return True
    return False

def estValeurSinguliereVerticale(A, n, x, y, epsilon, tol):
    matAugmentee = np.block([
        [x * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), A - x * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    for vap in vaps:
        if np.abs(vap - 1j*y) < tol:
            return True
    return False

def CrissCrossAbscisse(A, n, epsilon, nbPoints, tol):
    z1 = rightmostVap(A)

    #etape 2
    rechercheHorizontale = np.linspace(z1.real, z1.real + 1, nbPoints)
    for x in rechercheHorizontale:
        if estValeurSinguliereHorizontale(A, n, x, z1.imag, epsilon, tol):
            z1 = x + 1j*z1.imag
    zk = z1

    Y = np.append(Y, zk.imag)

    #etape 3: intersections verticales basses
    for _ in range(2*n):
        rechercheVerticale = np.linspace(zk.imag - 1, zk.imag, nbPoints)
        for y in rechercheVerticale:
            if estValeurSinguliereVerticale(A, n, zk.real, y, epsilon, tol):
                if np.abs(svmin(A, n, zk.real, y) - epsilon) < tol:
                    Y = np.insert(Y, 0, y)
                    zk = zk.real + 1j*y

    zk = z1

    #etape 3: intersections verticales hautes
    for _ in range(2*n):
        rechercheVerticale = np.linspace(zk.imag, zk.imag + 1, nbPoints)
        for y in rechercheVerticale:
            if estValeurSinguliereVerticale(A, n, zk.real, y, epsilon, tol):
                if np.abs(svmin(A, n, zk.real, y) - epsilon) < tol:
                    Y = np.append(Y, y)
                    zk = zk.real + 1j*y