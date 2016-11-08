import argparse
import struct
import numpy
import lshash
import reader

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()

f = open(args.filepath, 'rb')
#print(len(x))
#dim, = struct.unpack('i', f.read(4))

mat = reader.read_fvec(args.filepath)
print(mat.shape)
