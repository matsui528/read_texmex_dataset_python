import struct
import numpy

def read_base(filename, typechar, typesize):
    with open(filename, 'rb') as f:
        while True:
            vec = []
            d_bin = f.read(4)
            if d_bin=='':
                break
            dim, = struct.unpack('i', d_bin)
            for d in range(dim):
                value, = struct.unpack(typechar, f.read(typesize))
                vec.append(value)
            yield vec

#float
def read_fvec(filename):
    return numpy.array(list(read_fvec_iter(filename)))
def read_fvec_iter(filename):
    return read_base(filename, 'f', 4)

#unsigned char
def read_bvec(filename):
    return numpy.array(list(read_bvec_iter(filename)))
def read_bvec_iter(filename):
    return read_base(filename, 'B', 1)
