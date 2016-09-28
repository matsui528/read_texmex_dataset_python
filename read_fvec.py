import argparse
import struct
import numpy
import lshash

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()

f = open(args.filepath, 'rb')
#print(len(x))
#dim, = struct.unpack('i', f.read(4))

mat = []
while True:
    vec = []
    d_bin = f.read(4)
    if d_bin=='':
        break
    dim, = struct.unpack('i', d_bin)
    for d in range(dim):
        value, = struct.unpack('f', f.read(4))
        vec.append(value)
    mat.append(vec)
    if len(mat) % 1000 == 0:
        print len(mat)
mat = numpy.array(mat)
print mat.shape

lsh = lshash.LSHash(100, 128)
lshdata = []
for datum in mat:
    lshstring = lsh._hash(lsh.uniform_planes[0], datum)
    lshdata.append([int(x) for x in lshstring])
numpy.savetxt("sift_lsh.csv", lshdata, delimiter=",", fmt="%1d")

