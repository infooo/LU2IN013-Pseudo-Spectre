import numpy as np
import matplotlib.pyplot as plt
import math

#Algo Criss-Cross pour l'abscisse du pseudospectre (sup Re z, z dans le pseudospectre)

def rightmostVap(A):
    vaps = np.linalg.eig(A)[0]
    rmVap = max(vaps, key = lambda x: x.real)
    return rmVap 

def estValeurSinguliere(A, n, x, y, epsilon, tol):
    matAugmentee = np.block([
        [x * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), A - x * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    for vap in vaps:
        if np.abs(vap - 1j*y) < tol:
            return True
    return False