import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse
matplotlib.use('Agg')


operation_type = 'Make plot'

parser = argparse.ArgumentParser(
            description='Use with txt file.',
            prog='hist.py')

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the input file',
                    required=True)

parser.add_argument('--out_file',
                    type=str,
                    help='Name of the output file',
                    required=True)

parser.add_argument('--title',
                    type=str,
                    help='Title of the Graph',
                    required=True)

parser.add_argument('--x',
                    type=str,
                    help='Name of x axis',
                    required=True)

parser.add_argument('--y',
                    type=str,
                    help='Name of y axis',
                    required=True)


args = parser.parse_args()
data_file = args.file_name
out_file = args.out_file
title = args.title
x = args.x
y = args.y

D = []
for line in open(data_file):
    D.append(float(line))

fig, ax = plt.subplots()
ax.plot(D)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file, bbox_inches='tight')
