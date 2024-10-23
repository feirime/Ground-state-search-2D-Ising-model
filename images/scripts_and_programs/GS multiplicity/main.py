import os

import numpy as np
import matplotlib.pyplot as plt

dos_dir = "data/"
for file in os.listdir(dos_dir):
    file = dos_dir + file
    gem = np.loadtxt(open(file), skiprows=4).T
    N = int(open(file).readlines()[0].rstrip())
    J_sum = int(open(file).readlines()[2].rstrip())
    P_plus = (2 * N * (N - 1) + J_sum) / (4 * N * (N - 1))
    G, E, M = gem[0], gem[1], gem[2]
    plt.xlabel("Egs/NJ")
    plt.scatter(np.min(E) / (2 * N * (N - 1)), np.max(M[np.argwhere(E == np.min(E))]) / (N * N), color='black', s=10)
    plt.ylabel("Mmax/N")
    #plt.scatter(np.min(E) / (2 * N * (N - 1)), np.sum(G[np.argwhere(E == np.min(E))]), color='black', s=10)
    #plt.ylabel("Ggs")
    #plt.yscale("log")
plt.show()
