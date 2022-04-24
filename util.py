import numpy as np
import sympy as sym
import galois
from cryptography.fernet import Fernet
from sympy.polys import subresultants_qq_zz

n = 4
m = 3
deg = 11 # degree of the irreducible polynomial

GF = galois.GF(2 ** 8) # modular arithemtic uses finite field GF(2^8)
F = Fernet(Fernet.generate_key())
f_poly = galois.irreducible_poly(2 ** 8, deg, method='random')


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

def gen_fingerprint(F_coefs, fp_filename):
    x = sym.symbols('x')

    f_coefs = list(map(int, list(f_poly.coeffs)))
    F_coefs = list(map(int, F_coefs))

    size = deg + len(F_coefs)
    
    with open(fp_filename, 'wb') as f:
        for i in range(size):
            row = []

            if i in range(0, deg):
                row = f_coefs
                row.extend((n-1-i)*[0])
                row[:0] = [0]*i

            if i in range(deg, size):
                row = F_coefs
                row.extend((size-1-i)*[0])
                row[:0] = [0]*(size-len(row))

            f.write(bytes(row))

if __name__ == "__main__":
    # A = gen_encoding_matrix(6, 4)
    # print(A, type(A))
    # gen_fingerprint(list(f_poly.coeffs))
    pass