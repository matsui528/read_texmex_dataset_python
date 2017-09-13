import struct
import numpy
import os


def read_base(filename, typechar, typesize, skipsample=0):
    class ReadBaseIterator:
        def __init__(self, file, typechar, typesize, skipsample):
            self.f = file
            self.typechar = typechar
            self.typesize = typesize
            self.f.seek(0)
            if skipsample > 0:
                d_bin = self.f.read(4)
                dim, = struct.unpack('i', d_bin)
                self.f.seek(dim * typesize * skipsample + 4 * skipsample, 0)

        def __iter__(self):
            return self

        def next(self):
            return self.__next__()

        def __next__(self):
            d_bin = self.f.read(4)
            if d_bin == b'':
                raise StopIteration()
            dim, = struct.unpack('i', d_bin)
            vec = struct.unpack(self.typechar * dim, self.f.read(self.typesize * dim))
            return vec

        def next_without_unpack(self):
            d_bin = self.f.read(4)
            if d_bin == b'':
                raise StopIteration()
            dim, = struct.unpack('i', d_bin)
            return self.f.read(dim * self.typesize)

    return ReadBaseIterator(filename, typechar, typesize, skipsample)


def get_sample_size(filename, typechar, typesize):
    with open(filename, 'rb') as f:
        d_bin = f.read(4)
        dim, = struct.unpack('i', d_bin)
        return int(os.path.getsize(filename) / dim / typesize)


# float
def read_fvec(file):
    return numpy.array(list(read_fvec_iter(file)))


def read_fvec_iter(file, skipsample=0):
    return read_base(file, 'f', 4, skipsample=skipsample)


def get_fvec_size(file):
    return get_sample_size(file, 'f', 4)


# unsigned char
def read_bvec(file):
    return numpy.array(list(read_bvec_iter(file)))


def read_bvec_iter(file, skipsample=0):
    return read_base(file, 'B', 1, skipsample=skipsample)


def get_bvec_size(file):
    return get_sample_size(file, 'B', 1)
