import argparse
import struct
import numpy
import reader
import csv
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("savepath")
parser.add_argument("--split", type=int)
args = parser.parse_args()

def process(input_path, output_path, offset, count):
    with open(output_path, "w+") as fw:
        writer = csv.writer(fw)
        for i,vec in enumerate(reader.read_fvec_iter(args.filepath, skipsample=offset)):
            if i % 100000 == 0:
                print(i)
            if i == count:
                break
            writer.writerow(vec)

if __name__ == '__main__':
    if args.split is None:
        args.split = reader.get_fvec_size(args.filepath)
        print(args.split)
    processes = []
    for i in xrange(0, reader.get_fvec_size(args.filepath), args.split):
        p = multiprocessing.Process(target=process, args=(
            args.filepath, 
            "{}_{}".format(args.savepath, i),
            i,
            args.split
        ))
        processes.append(p)
        p.start()
        print("started")
    for process in processes:
        process.join()
