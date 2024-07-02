import os
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import configparser

import numpy as np


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
if conf["Plot"]["plot"] == "Egs_size":
    for size in range(5, 10):
        directory = dos_dir + str(size ** 2) + "/"
        file_count = 0
        arr_of_files = numpy.array([])
        J_sum = numpy.array([])
        P_plus = numpy.array([])
        max_gem_size = 0
        for file in os.listdir(directory):
            file = directory + file
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
            plt.scatter(1/size**2, numpy.min(E)/(N * (N - 1)), color=colors[size-5])
if conf["Plot"]["plot"] == "Egs_P":
    directory = dos_dir + conf["Sample"]["spins"] + "/"
    file_count = 0
    arr_of_files = numpy.array([])
    J_sum = numpy.array([])
    P_plus = numpy.array([])
    for file in os.listdir(directory):
        file = directory + file
        arr_of_files = numpy.append(arr_of_files, file)
        N = int(open(file).readlines()[0].rstrip())
        J_sum = numpy.append(J_sum, int(open(file).readlines()[2].rstrip()))
        P_plus = numpy.append(P_plus, (2 * N * (N - 1) + J_sum[file_count]) / (4 * N * (N - 1)))
        file_count += 1
    idx = P_plus.argsort()
    J_sum = J_sum[idx]
    P_plus = P_plus[idx]
    arr_of_files = arr_of_files[idx]
    for i in range(file_count):
        file = arr_of_files[i]
        gem = numpy.loadtxt(open(file), skiprows=4).T
        E = gem[1]
        plt.scatter(P_plus[i], numpy.min(E)/(N * (N - 1)), s=5, color='black')
if conf["Plot"]["plot"] == "Ggs_size":
    for size in range(5, 10):
        directory = dos_dir + str(size ** 2) + "/"
        file_count = 0
        arr_of_files = numpy.array([])
        J_sum = numpy.array([])
        P_plus = numpy.array([])
        max_gem_size = 0
        for file in os.listdir(directory):
            file = directory + file
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
            G = gem[0]
            E = gem[1]
            Egs = np.min(E)
            Ggs = numpy.sum(G[np.isin(E, Egs)])
            plt.scatter(1/size**2, Ggs, color=colors[size-5])
if conf["Plot"]["plot"] == "Ggs_P":
    directory = dos_dir + conf["Sample"]["spins"] + "/"
    file_count = 0
    arr_of_files = numpy.array([])
    J_sum = numpy.array([])
    P_plus = numpy.array([])
    for file in os.listdir(directory):
        file = directory + file
        arr_of_files = numpy.append(arr_of_files, file)
        N = int(open(file).readlines()[0].rstrip())
        J_sum = numpy.append(J_sum, int(open(file).readlines()[2].rstrip()))
        P_plus = numpy.append(P_plus, (2 * N * (N - 1) + J_sum[file_count]) / (4 * N * (N - 1)))
        file_count += 1
    idx = P_plus.argsort()
    J_sum = J_sum[idx]
    P_plus = P_plus[idx]
    arr_of_files = arr_of_files[idx]
    for i in range(file_count):
        file = arr_of_files[i]
        gem = numpy.loadtxt(open(file), skiprows=4).T
        G = gem[0]
        E = gem[1]
        Egs = np.min(E)
        Ggs = numpy.sum(G[np.isin(E, Egs)])
        Ggs = numpy.log(Ggs)
        plt.scatter(P_plus[i], Ggs, s=5, color='black')
plt.show()
