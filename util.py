import numpy as np
from mod import Mod
from sympy import Matrix

p = 257 # take 257 as the prime

def encoding_matrix(n, m):
    """Create an n x m encoding matrix.
    Parameters:
        n: the number of fragments to output
        m: the number of fragments required for reconstruction
    Returns:
        the encoding matrix
    """
    A = np.zeros((n, m)).astype(int)
    for i in range(n):
        x = Mod(i, p)
        for j in range(m):
            A[i, j] = (x + 1) ** j
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
    res = np.zeros((m1.shape[0], m2.shape[1])).astype(int)
    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            tmp = Mod(0, p)
            for k in range(m1.shape[1]):
                tmp = tmp + Mod(m1[i, k], p) * Mod(m2[k, j], p)
            res[i, j] = tmp
    return res

def inverse(m):
    """calculate the inverse of a matrix
    Parameters:
        m: the matrix
    Returns:
        The inverse of m
    """
    return Matrix(m).inv_mod(p)