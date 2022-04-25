import os
import sys
import argparse
import numpy as np
from util import *

parser = argparse.ArgumentParser()
parser.add_argument('frag_dir', help='the directory containing the dispersed fragments')

def reconstruct(frag_dir):
    if len(os.listdir(frag_dir)) < m:
        print("m={} fragments are needed for reconstructing the file !".format(str(m)))
        sys.exit(1)

    B = [] # decoding matrix
    fragments = []
    
    for i, filename in enumerate(os.listdir(frag_dir)):
        if i >= m:
            break
        with open(frag_dir + filename, 'rb') as f:
            content = F.decrypt(f.read())
            header, payload, signature = content[:3], content[3:-32], content[-32:]
            B.append(GF(list(header)))

            # authenticate the fragment
            if signature != gen_HMAC(content[:-32]):
                print("Unable to authenticate fragment file '{}'".format(filename))
                return

            fragments.append(GF(list(payload)))

    B = np.linalg.inv(GF(B))
    fragments = GF(fragments)

    output = B @ fragments

    # recover the original byte array
    segments = []
    for col in range(len(output[0])):
        segments.extend([row[col] for row in output])
    
    # remove padded 0s
    while segments[-1] == 0:
        segments.pop()

    plaintext = bytearray(segments).decode()
    with open("output", "w") as f:
        f.write(plaintext)


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    reconstruct(args.frag_dir)