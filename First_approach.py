import numpy as np
import matplotlib.pyplot as plt
import math

def Pseudo(x, y, A, n, epsilon):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def affichage(n, epsilon):

    A = np.random.rand(n, n)*10-5
    R = [2*math.sqrt(n)*epsilon + np.sum(np.abs(A[i, :])) for i in range(n)]
    centres = np.diag(A)

    x = np.array([])
    y = np.array([])
    seen = set()
    for i in range(n):
        re = centres[i].real
        im = centres[i].imag
        leftbound = re - R[i]
        rightbound = re + R[i]
        upperbound = im + R[i]
        lowerbound = im - R[i]
        arrx = np.linspace(leftbound, rightbound, 100)
        arry = np.linspace(lowerbound, upperbound, 100)
        X, Y = np.meshgrid(arrx, arry)
        Z = np.empty_like(X, dtype=float)
        
        for i in range(len(arrx)):
            for j in range(len(arry)):
                if (i, j) not in seen:
                    Z[j, i] = Pseudo(X[j, i], Y[j, i], A, n, epsilon)
                    seen.add((i,j))

        C = epsilon
        plt.contour(X, Y, Z, levels=[C, 10*C], colors=['blue', 'red'])
        plt.xlabel('Reels')
        plt.ylabel('Imaginaires')
        plt.title('Contours du pseudo-spectre')
        plt.grid(True)

