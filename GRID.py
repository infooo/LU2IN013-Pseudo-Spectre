import numpy as np
import matplotlib.pyplot as plt
import math

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def svmin(x, y, A, n):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def affichage(n, A, epsilon, nbPoints):

    R = [math.sqrt(n)*epsilon + np.sum(np.abs(A[i, :])) for i in range(n)]
    centers = np.diag(A)

    x = np.array([])
    y = np.array([])
    seen = set()
    for i in range(n):
        re = centers[i].real
        im = centers[i].imag
        leftbound = re - R[i]
        rightbound = re + R[i]
        upperbound = im + R[i]
        lowerbound = im - R[i]
        arrx = np.linspace(leftbound, rightbound, nbPoints)
        arry = np.linspace(lowerbound, upperbound, nbPoints)
        X, Y = np.meshgrid(arrx, arry)
        Z = np.empty_like(X, dtype=float)
        
        for i in range(len(arrx)):
            for j in range(len(arry)):
                if (i, j) not in seen:
                    Z[j, i] = svmin(X[j, i], Y[j, i], A, n)
                    seen.add((i,j))
                else:
                    Z[j, i] = 1000

        C = epsilon
        plt.contour(X, Y, Z, levels=[10*C], colors=['blue'])
        plt.xlabel('Reels')
        plt.ylabel('Imaginaires')
        plt.title('Contour du pseudo-spectre')
        plt.grid(True)

