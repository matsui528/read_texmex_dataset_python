import argparse
import csv

from texmex import reader

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("save_basepath")
parser.add_argument("split", type=int)
args = parser.parse_args()

for i, vec in enumerate(reader.read_bvec_iter(args.filepath)):
    if i % args.split == 0:
        fw = open("{}_split{}".format(args.save_basepath, i/args.split), "w+")
        writer = csv.writer(fw)
    writer.writerow(vec)
