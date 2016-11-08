# -*- coding: utf-8 -*-
import struct


class Writer(object):
    def __init__(self, filename, typechar):
        self.file = open(filename, "wb+")
        self.typechar = typechar

    def write(self, vec):
        self.file.write(struct.pack('i', len(vec)))
        self.file.write(struct.pack(self.typechar * len(vec), *vec))
