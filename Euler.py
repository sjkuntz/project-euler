from bitarray import bitarray
import numpy as np

def esieve(n):
    """Find all primes less than `n' with the Sieve of Eratosthenes. Attempts to
    be memory and CPU efficient by using a `bitarray' to store whether or not an
    integer is prime.
    """
    if n<=2:
        return np.array([])

    isprime = bitarray(n//2)
    isprime.setall(True)

    for k in range(3,int(n**0.5)+1,2):
        if isprime[k//2]:
            isprime[k*k//2::k] = False

    return np.array([2] + [2*i+1 for i in range(1,n//2) if isprime[i]],dtype=int)

assert esieve(2).size == 0
assert esieve(3) == [2]
assert(esieve(10) == [2,3,5,7]).all()
assert(esieve(20) == [2,3,5,7,11,13,17,19]).all()
