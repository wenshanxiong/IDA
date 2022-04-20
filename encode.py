import util

def encode(n, m, msg):
    """Encodes the given message and returns the fragments
    Parameters:
        n: the number of fragments to output
        m: the number of fragments required for reconstruction
        msg: the message to encode
    Returns:
        A list n fragments, each of size [l/m]
    """
    # convert msg into byte array
    l = bytearray(msg, 'utf-8')

    # split l into segments of size m
    segments = [list(l[i:i+m]) for i in range(0,len(l),m)]

    # pad last segment so that all segments have size m
    segments[-1] += [0] * (m - len(segments[-1]))

    # TODO
    # A = util.encoding_matrix()

    # TODO
    # output = A @ segments.T
    # return output
    print(segments)


encode(3,3,'hello!!')