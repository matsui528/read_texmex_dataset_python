# -*- coding: utf-8 -*-
import csv
import argparse
import os
import pipe
import texmex_python

parser = argparse.ArgumentParser()
parser.add_argument("csv_path")
parser.add_argument("fvec_path")
args = parser.parse_args()
assert not os.path.exists(args.fvec_path)

writer = texmex_python.Writer(args.fvec_path, 'f')

with open(args.csv_path) as fr:
    reader = csv.reader(fr)
    for vec in reader | pipe.select(lambda vec: list(map(float, vec))):
        writer.write(vec)
