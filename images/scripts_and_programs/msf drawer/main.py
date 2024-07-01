import numpy as np
from matplotlib import pyplot as plt


def sq(arr):
    return arr.reshape((-1, int(np.sqrt(arr.shape[0]))))


array = np.loadtxt("data/XMCD#0000..txt.dat")
qx = sq(array[:, 1])
qy = sq(array[:, 2])
re = sq(array[:, 3])
plt.figure(dpi=300)
plt.gca().set_aspect('equal')
plt.xlabel("$q_x$")
plt.ylabel("$q_y$")
plt.pcolormesh(qx, qy, re, cmap='inferno')
plt.colorbar()
plt.show()
