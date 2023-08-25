import numpy as np

def QR_Decomp(A, n):
    Q = np.zeros((n, n))
    R = np.zeros((n, n))
    Q[:, 0] = A[:, 0]/np.linalg.norm(A[:, 0])
    R[0, 0] = np.linalg.norm(A[:, 0])
    for i in range(1, n):
        Q[:, i] = A[:, i]
        for j in range(i):
            Q[:, i] -= (Q[:, j].T @ A[:, i]) * Q[:, j]
            R[j, i] = (Q[:, j].T @ A[:, i])
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:, i]/np.linalg.norm(Q[:, i])
    return Q, R


n = int(input())
A = np.zeros((n, n))

for i in range(n):
    A[i] = [float(i) for i in input().split()]

for i in range(1000):
    Q, R = QR_Decomp(A, n)
    A = R @ Q
eigenvalues = [A[i, i] for i in range(n)]

det = 1
for i in range(n):
    det *= eigenvalues[i]


for i in sorted(eigenvalues):
    print("{:.3f}".format(i), end= " ")
print()
print("{:.3f}".format(det))