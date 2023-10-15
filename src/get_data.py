import sys
import argparse

operation_type = 'Get data'

parser = argparse.ArgumentParser(
            description='Use with CSV file.',
            prog='get_data.py')

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the file',
                    required=True)

parser.add_argument('--country',
                    type=str,
                    help='Name of the country of interest',
                    required=True)

parser.add_argument('--out_file',
                    type=str,
                    help='Name of the output file',
                    required=True)

args = parser.parse_args()
file_name = args.file_name
country_name = args.country
out_file = args.out_file


f = open(out_file, 'w')
for line in open(file_name):
    A = line.rstrip().split(',')
    if A[0] == country_name:
        f.write(str(float(A[11])) + '\n')
