import util

def encode(n, m, msg):
    # convert msg into byte array
    l = bytearray(msg, 'utf-8')

    # split l into segments of size m
    segments = [list(l[i:i+m]) for i in range(0,len(l),m)]

    # pad last segment so that all segments have size m
    segments[-1] += [0] * (m - len(segments[-1]))

    
    A = util.encoding_matrix()
    output = A @ segments.T # not sure about this yet.
    print(segments)



encode(3,3,'hello!!')