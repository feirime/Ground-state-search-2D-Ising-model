import numpy
import numpy as np

file = "gem_glass100_J0_0.dat"
gem = numpy.loadtxt(open(file), skiprows=4).T
G = gem[0]
E = gem[1]
M = gem[2]
M_gs_idx = np.argwhere(E == np.min(E))
print(M_gs_idx)
M_gs = M[M_gs_idx]
G_gs = G[np.isin(M, M_gs)]
print(np.sum(G_gs) / 2**100)
