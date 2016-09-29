import argparse
import struct
import numpy
import reader
import csv

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("savepath")
args = parser.parse_args()

with open(args.savepath, "w+") as fw:
    writer = csv.writer(fw)
    for i, vec in enumerate(reader.read_fvec_iter(args.filepath)):
        if i % 100000 == 0:
            print(i)
        writer.writerow(vec)
