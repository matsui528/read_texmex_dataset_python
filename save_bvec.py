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
    for vec in reader.read_bvec_iter(args.filepath):
        writer.writerow(vec)
