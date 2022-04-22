import numpy as np
import galois

GF = galois.GF(2 ** 8) # modular arithemtic uses finite field GF(2^8)

def encoding_matrix(n, m):
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

def decoding_matrix(A, fragmentIDs):
    """Create an m x m decoding matrix
    Parameters:
        A: the encoding matrix
        fragmentIDs: a list of fragments' IDs for making decoding matrix
    Returns:
        the decoding matrix
    """
    return inverse(A[fragmentIDs, ])

def dot_product(m1, m2):
    """calculate the dot product of m1 and m2
    Parameters:
        m1: the first matrix
        m2: the second matrix
    Returns:
        The dot product of m1 and m2.
    """
    return m1 @ m2

def inverse(m):
    """calculate the inverse of a matrix
    Parameters:
        m: the matrix
    Returns:
        The inverse of m
    """
    return np.linalg.inv(m)


if __name__ == "__main__":
    A = encoding_matrix(6, 4)
    print(A, type(A))

    B = decoding_matrix(A, [0,1,2,3])
    print(B, type(B))

    print(dot_product(A[[0,1,2,3],], B))