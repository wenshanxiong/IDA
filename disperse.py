import os
import sys
import argparse
from util import *

parser = argparse.ArgumentParser()
parser.add_argument('inputFile', help='the input filename')

def disperse(filename, n=4, m=3):
    A = None
    fragment_matrix = None

    with open(filename, 'rb') as f:
        # split file into segments of size m
        payload = list(f.read())
        for _ in range(m - len(payload) % m):
            payload.append(0)
        segments = [payload[i:i+m] for i in range(0, len(payload), m)]
        segments = GF(segments)

        A = encoding_matrix(n, m)
        
        fragment_matrix = dot_product(A, segments.T)
        
        print(A)
        print(fragment_matrix)

    # write fragments to files
    for i in range(n):
        out_filename = "./fragments/" + str(i)
        os.makedirs(os.path.dirname(out_filename), exist_ok=True)
        with open(out_filename, 'wb') as f:
            f.write(bytes(list(A[i]) + list(fragment_matrix[i])))


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    disperse(args.inputFile)
    