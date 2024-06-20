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
dos_dir = "../../dos" + conf["Sample"]["spins"] + "glass/"
stat_dir = "data/statsum" + conf["Sample"]["spins"] + "/"
fig_dir = "data/figures" + conf["Sample"]["spins"] + "/"
H = numpy.linspace(float(conf["Field"]["start"]),
                   float(conf["Field"]["stop"]),
                   int(conf["Field"]["steps"]))
P_plus = numpy.array([])
J_sum = numpy.array([])
file_count = 0
max_gem_size = 0
arr_of_files = numpy.array([])
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
plt.figure(dpi=300)
