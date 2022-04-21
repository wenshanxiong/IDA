from pydoc import plain
import util
from util import *

def decode(fragments, A):
    """Decode the given fragments and returns the plaintext message
    Parameters:
        fragments: the fragments produced by the encode function
        A: the encoding matrix used for creating fragments
    Returns:
        The plaintext message
    """

    # TODO: fragmentIDs should be taken as an argument to function 'decoding_matrix'
    #       (each row of arg 'fragments' should be assigned with an ID)
    #       (recommendation: turn fragments into a dict with keys as ID)
    fragmentIDs = fragments.keys()
    B = decoding_matrix(A, fragmentIDs)
    output = dot_product(inverse(B), fragments)

    # recover the original byte array
    segments = []
    for col in len(output[0]):
        segments.extend([row[col] for row in output])
    
    # remove padded 0s
    while segments[-1] == 0:
        segments.pop()

    plaintext = bytearray(segments)
    print(plaintext)
    return plaintext

decode(None, None)