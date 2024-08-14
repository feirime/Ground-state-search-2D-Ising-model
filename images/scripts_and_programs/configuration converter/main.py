import os
import math

def create_files(file_path, output_dir):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line.startswith('cell'):
                folder_name = line.strip().split('.')[0]
                output_folder = os.path.join(output_dir, folder_name)
                os.makedirs(output_folder, exist_ok=True)
            elif set(line.strip()) <= set('1-') and len(line) > 5:
                file_name = os.path.join(output_folder, f'{line_number}.txt')
                n = int(math.sqrt(int(folder_name[4:6])))
                with open(file_name, 'a') as out_file:
                    gs = []
                    swich = True
                    for char in line:
                        if char == '1' and swich:
                            gs.append(1)
                        swich = True
                        if char == '-':
                            swich = False
                            gs.append(-1)
                    print(gs)
                    for i in range(n):
                        for j in range(n):
                            out_file.write(str(i) + '\t')
                            out_file.write(str(j) + '\t')
                            out_file.write(str(gs[i * n + j]) + '\t')
                            out_file.write('0 \t')
                            out_file.write('0 \n')
                

file_path = 'data/S81_2.txt'
output_dir = 'data'

create_files(file_path, output_dir)