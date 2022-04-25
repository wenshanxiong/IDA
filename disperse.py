import os
import sys
import argparse
from util import *

parser = argparse.ArgumentParser()
parser.add_argument('inputFile', help='the input filename')

def disperse(filename):
    A = None
    fragment_matrix = None

    # perform fragmentation
    with open(filename, 'rb') as f:
        # split file into segments of size m
        payload = list(f.read())
        for _ in range(m - len(payload) % m):
            payload.append(0)
        segments = [payload[i:i+m] for i in range(0, len(payload), m)]
        segments = GF(segments)

        A = gen_encoding_matrix(n, m)
        
        fragment_matrix = A @ segments.T

    # write fragments to files & create signature for each fragment
    for i in range(n):
        frag_filename = "./fragments/" + str(i)
        os.makedirs(os.path.dirname(frag_filename), exist_ok=True)

        with open(frag_filename, 'wb') as f:
            payload = list(A[i]) + list(fragment_matrix[i])
            signature = gen_HMAC(bytes(payload))

            # file content: header | fragment | signature
            content = bytes(payload) + signature
            f.write(F.encrypt(content))


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    disperse(args.inputFile)
    