import struct
import numpy
import os

def read_base(filename, typechar, typesize, skipsample=0):
    with open(filename, 'rb') as f:
        if skipsample > 0:
            d_bin = f.read(4)
            dim, = struct.unpack('i', d_bin)
            f.seek(dim*typesize*skipsample + 4*skipsample, 0)
        while True:
            vec = []
            d_bin = f.read(4)
            if d_bin==b'':
                break
            dim, = struct.unpack('i', d_bin)
            # f.read(dim*typesize)
            for d in range(dim):
               value, = struct.unpack(typechar, f.read(typesize))
               vec.append(value)
            yield vec

def get_sample_size(filename, typechar, typesize):
    with open(filename, 'rb') as f:
        d_bin = f.read(4)
        dim, = struct.unpack('i', d_bin)
        return os.path.getsize(filename) / dim /typesize


#float
def read_fvec(filename):
    return numpy.array(list(read_fvec_iter(filename)))
def read_fvec_iter(filename, skipsample=0):
    return read_base(filename, 'f', 4, skipsample=skipsample)
def get_fvec_size(filename):
    return get_sample_size(filename, 'f', 4)

#unsigned char
def read_bvec(filename):
    return numpy.array(list(read_bvec_iter(filename)))
def read_bvec_iter(filename):
    return read_base(filename, 'B', 1)
