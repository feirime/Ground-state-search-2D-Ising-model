import re
import math


def read_alternate_lines(file_in):
    with open(file_in, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    pattern = re.compile(r'^cell')
    result_lines = []
    names = []
    for i, line in enumerate(lines):
        if pattern.match(line):
            names.append('GSes' + lines[i].strip('cell'))
            if i + 1 < len(lines):
                result_lines.append(lines[i + 1].strip())
                for j in range(i + 4, len(lines), 3):
                    if pattern.match(lines[j]):
                        break
                    if j < len(lines):
                        result_lines.append(lines[j].strip())
                        names.append('GSes' + lines[i].strip('cell'))
    return result_lines, names


def write_data(gses, cell_names):
    for i in range(len(gses)):
        with open(cell_names[i].rstrip('\n'), 'a', encoding='utf-8') as file:
            file.write(gses[i] + '\n')


def transform_to_msf(gses, cell_names):
    #for gs_idx in range(len(gses)):
    for gs_idx in range(1):
        n = int(cell_names[gs_idx][4:6])
        n = int(math.sqrt(n))
        out_file = open(cell_names[gs_idx].strip(), 'a', encoding='utf-8')
        for i in range(n):
            for j in range(n):
                out_file.write(str(i) + '\t')
                out_file.write(str(j) + '\t')
                out_file.write(str(gses[gs_idx][i * n + j]) + '\t')
                out_file.write('0 \t')
                out_file.write('0 \n')


file_conf = 'data/S81_2.txt'
ground_states, samples = read_alternate_lines(file_conf)
#write_data(ground_states, samples)
transform_to_msf(ground_states, samples)
