import sympy as sym
import galois
import hmac
from cryptography.fernet import Fernet
from hashlib import sha256
from math import ceil
import unireedsolomon as rs

n = 4
m = 3
deg = 11 # degree of the irreducible polynomial
block_length = 255
msg_length = 64

coder = rs.RSCoder(block_length, msg_length)
chunk_size = ceil(block_length / n)
fingerprint_size = chunk_size * n

sec_key = b'o7FUu9QB4D94gYnPDr7BHs0TxlvKvFiNtUYcebJJt0s='
GF = galois.GF(2 ** 8) # modular arithemtic uses finite field GF(2^8)
F = Fernet(sec_key)
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

def gen_HMAC(payload):
    h = hmac.new(sec_key, payload, sha256)
    return h.digest()

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

def gen_hash(payload):
    return sha256(payload).hexdigest()

def gen_rs_code(payload):
    return coder.encode(payload)

def recover_rs_code(payload):
    return coder.decode(payload)

def gen_distributed_fingerprint(hashes):
    rs_codes = [gen_rs_code(h) + "0" * (n - block_length % n) for h in hashes]
    distributed_fingerprint = []
    for i in range(n):
        distributed_fingerprint.append('')
        for j in range(n):
            distributed_fingerprint[i] += rs_codes[j][i*chunk_size: (i+1)*chunk_size]
    return distributed_fingerprint

def recover_hashes(distributed_fingerprint):
    retrived_rs = []
    for i in range(n):
        retrived_rs.append('')
        for j in range(n):
            if distributed_fingerprint[j] == None or len(distributed_fingerprint[j]) != fingerprint_size:
                retrived_rs[i] += "0" * chunk_size
            else:
                retrived_rs[i] += distributed_fingerprint[j][i * chunk_size: (i+1) * chunk_size]
        retrived_rs[i] = retrived_rs[i][:block_length]

    recovered_hashes = []
    for rs_code in retrived_rs:
        recovered_hashes.append(recover_rs_code(rs_code)[0])
    return recovered_hashes

if __name__ == "__main__":
    # A = gen_encoding_matrix(6, 4)
    # print(A, type(A))
    pass