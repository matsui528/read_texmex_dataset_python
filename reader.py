import struct
import numpy
import os


def read_base(filename, typechar, typesize, skipsample=0):
    class ReadBaseIterator:
        def __init__(self, filename, typechar, typesize, skipsample):
            self.f = open(filename, 'rb')
            self.typechar = typechar
            self.typesize = typesize
            if skipsample > 0:
                d_bin = self.f.read(4)
                dim, = struct.unpack('i', d_bin)
                self.f.seek(dim*typesize*skipsample + 4*skipsample, 0)

        def __iter__(self):
            return self

        def next(self):
            return self.__next__()

        def __next__(self):
            vec = []
            d_bin = self.f.read(4)
            if d_bin==b'':
                raise StopIteration()
            dim, = struct.unpack('i', d_bin)
            for d in range(dim):
               value, = struct.unpack(self.typechar, self.f.read(self.typesize))
               vec.append(value)
            return vec

        def next_without_unpack(self):
            vec = []
            d_bin = self.f.read(4)
            if d_bin==b'':
                raise StopIteration()
            dim, = struct.unpack('i', d_bin)
            return self.f.read(dim*self.typesize)
    return ReadBaseIterator(filename, typechar, typesize, skipsample)

def get_sample_size(filename, typechar, typesize):
    with open(filename, 'rb') as f:
        d_bin = f.read(4)
        dim, = struct.unpack('i', d_bin)
        return int(os.path.getsize(filename) / dim /typesize)

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
def read_bvec_iter(filename, skipsample=0):
    return read_base(filename, 'B', 1, skipsample=skipsample)
def get_bvec_size(filename):
    return get_sample_size(filename, 'B', 1)
