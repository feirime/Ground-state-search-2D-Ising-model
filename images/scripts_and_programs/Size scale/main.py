import os
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import configparser


def colorFader(mix=0):
    c1 = numpy.array(mpl.colors.to_rgb('blue'))
    c2 = numpy.array(mpl.colors.to_rgb('red'))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


conf = configparser.ConfigParser()
conf.read("conf.ini")
dos_dir = "../../../../../DOS/dos"
stat_dir = "data/statsum" + conf["Sample"]["spins"] + "/"
plt.figure(dpi=int(conf["Plot"]["dpi"]))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
if conf["Plot"]["plot"] == "Energy_size":
    for size in range(5, 10):
        dos_dir = dos_dir + str(size ** 2) + "/"
        file_count = 0
        arr_of_files = numpy.array([])
        J_sum = numpy.array([])
        P_plus = numpy.array([])
        max_gem_size = 0
        for file in os.listdir(dos_dir):
            file = dos_dir + file
            arr_of_files = numpy.append(arr_of_files, file)
            N = int(open(file).readlines()[0].rstrip())
            J_sum = numpy.append(J_sum, int(open(file).readlines()[2].rstrip()))
            P_plus = numpy.append(P_plus, (2 * N * (N - 1) + J_sum[file_count]) / (4 * N * (N - 1)))
            file_count += 1
        idx = P_plus.argsort()
        J_sum = J_sum[idx]
        P_plus = P_plus[idx]
        arr_of_files = arr_of_files[idx]
        for i in range(int(conf["Sample"]["sample_in_group"])):
            sample = int(file_count * float(conf["Plot"]["P"]))
            file = arr_of_files[sample]
            gem = numpy.loadtxt(open(file), skiprows=4).T
            E = gem[1]
            plt.scatter(numpy.min(E), size, color=colors[size-5])
plt.show()
