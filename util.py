import numpy as np
import galois

n = 4
m = 3
GF = galois.GF(2 ** 8) # modular arithemtic uses finite field GF(2^8)

def gen_encoding_matrix(n, m):
    """Create an n x m encoding matrix.
    Parameters:
        n: the number of fragments to output
        m: the number of fragments required for reconstruction
    Returns:
        the encoding matrix
    """
    A = GF([[1 for _ in range(m)] for _ in range(n)])
    for i in range(n):
        A[i,] += GF(i)
    for j in range(m):
        A[:,j] = A[:,j] ** j
    return A


if __name__ == "__main__":
    A = gen_encoding_matrix(6, 4)
    print(A, type(A))