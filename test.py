from encode import encode
from decode import decode

if __name__ == "__main__":
    n = 4
    m = 3
    msg = "welcome to cs598ftd! this is a secret"
    fragments, A = encode(n, m, msg)
    fragmentIDs = [i for i in range(m)]
    print(decode(fragments[:m], fragmentIDs, A))