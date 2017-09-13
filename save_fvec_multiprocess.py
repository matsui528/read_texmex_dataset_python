import argparse
import csv
import multiprocessing

from texmex_python import reader

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
    num_samples = reader.get_fvec_size(args.filepath)
    if args.split is None:
        args.split = num_samples
    processes = []
    for i in xrange(0, num_samples, args.split):
        p = multiprocessing.Process(target=process, args=(
            open(args.filepath),
            ("{}_{:0"+str(len(str(num_samples)))+"d}").format(args.savepath, i),
            i,
            args.split
        ))
        processes.append(p)
        p.start()
        print("started")
    for process in processes:
        process.join()
