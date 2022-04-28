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

    cypher_payloads = []
    fingerprints = []
    
    for i in range(n):
        with open(frag_dir + str(i), 'rb') as f:
            content = f.read()
            cypher_payload = content

        cypher_payloads.append(cypher_payload)
        with open(frag_dir + str(i) + 'rs', 'r') as f:
            fingerprint = f.read()
            fingerprints.append(fingerprint)

    print(fingerprints)

    recovered_hashes = recover_hashes(fingerprints)
    B = [] # decoding matrix
    fragments = []
    for i in range(n):
        if len(fragments) >= m:
            break
        hash = gen_hash(cypher_payloads[i])
        if hash == recovered_hashes[i]:
            plaintext_payload = F.decrypt(cypher_payloads[i])
            header, payload = plaintext_payload[:3], plaintext_payload[3:]
            B.append(GF(list(header)))
            fragments.append(GF(list(payload)))
        else:
            print(hash, recovered_hashes[i])
            print("fragment {} is corrupted".format(i))

    if len(fragments) < m:
        print("Not enough valid fragments ({}/{}). Cannot reconstruct file".format(len(fragments), m))

    print(B)

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