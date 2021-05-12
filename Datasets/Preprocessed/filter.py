import os
import sys

filter_path = os.path.dirname(os.path.realpath(sys.argv[0])) + os.path.sep
output_path = filter_path + 'filtered/'

if not os.path.exists(output_path):
            os.makedirs(output_path)

files = [filter_path + 'dev_sets.tsv', filter_path + 'test_sets.tsv', filter_path + 'train_sets.tsv']

for f in files:
    tsv_in = open(f, 'r')
    tsv_out = open(output_path + f.split(filter_path)[1], 'w')

    for line in tsv_in:
        #This should be refined in the future
        if 'https' in line or 'http' in line:
            continue
        tsv_out.write(line)