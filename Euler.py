"""Euler
This module provides common functions necessary to solve the Project Euler
problems.
"""

# Written by Steven Kuntz <stevenjkuntz@gmail.com>
# License: GNU

from bitarray import bitarray
from functools import reduce
import numpy as np
from math import log, sqrt

# Problems 1, 6, 12
def triangular(n):
    """Find the ``n``th triangular number.

    ``T_n = 1 + 2 + ... + n``

    Parameters
    ----------
    n : int
        index

    Returns
    -------
    T_n :
        returns the ``n``th triangular number
    """
    return n*(n+1)//2

assert triangular(1)==1
assert triangular(2)==3
assert triangular(100)==5050

# Problem 5
def lcm(a,b=None):
    """Find the least common multiple of a list of integers, recursively.

    Parameters
    ----------
    a : int or array-like
        either the first integer argument, or a list of integers to be called on
        recursively

    b : int
        an argument for the second integer

    Returns
    -------
    multiple : int
        returns the lcm of the list or arguments
    """
    return reduce(lcm, a) if b is None else a*b//gcd(a,b)

# Problems 5, 8
def gcd(a,b):
    """Find the greatest common divisor of two integers.

    Parameters
    ----------
    a : int or array-like
        an argument for the first integer

    b : int
        an argument for the second integer

    Returns
    -------
    divisor : int
        returns the gcd of the arguments
    """
    while b!=0:
        (a,b) = (b,a%b)
    return a

# Problems 5, 10, 26
def esieve(n):
    """Find all primes less than ``n`` with the Sieve of Eratosthenes. Saves
    memory by using a ``bitarray`` to store whether or not an integer is prime.

    Parameters
    ----------
    n : int
        Upper bound

    Returns
    -------
    primes :
        returns a list of primes
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

# Problems 6,
def square_pyramidal(n):
    """Find the `n'th square pyramidal number."""
    return n*(n+1)*(2*n+1)//6

assert square_pyramidal(1)==1
assert square_pyramidal(2)==5
assert square_pyramidal(4)==30

# Problem 7
def prime_bounds(n):
    """Find the lower and upper bounds of the ``n``th prime.

    Parameters
    ----------
    n : int
        Upper bound

    Returns
    -------
    bounds : list, length = 2
        returns the upper and lower bound for the ``n``th prime
    """
    assert type(n)==int and n>=1, "n must be a positive integer."
    if n<6:
        return [1,14]
    else:
        lim = log(n)+log(log(n))
        return [int(n*(lim-1)),int(n*lim+1)]

assert prime_bounds(4) == [1,14]
assert prime_bounds(6) == [8,15]
assert prime_bounds(10) == [21,32]

# Problem 9, 39, 75
def pythagorean_triples_from_sum(s):
    """Find all Pythagorean triples `a^2+b^2=c^2' such that `a+b+c=s' and
    `0<a<b<c<s'.
    """
    if s%2==1 or s<12:
        return []
    trip = []
    for m in range(2,int((s/2)**0.5)+1):
        if (s//2)%m==0:
            if m%2==0:
                k = m+1
            else:
                k = m+2
            while (k < 2*m) and k <= s/(2*m):
                if (s//(2*m))%k==0 and gcd(m,k)==1:
                    d = s//(2*k*m)
                    n = k - m
                    a = d*(m**2-n**2)
                    b = d*2*m*n
                    c = d*(m**2+n**2)
                    trip += [(min(a,b),max(a,b),c)]
                k += 2
    return trip

assert pythagorean_triples_from_sum(12)[0]==(3,4,5)
assert pythagorean_triples_from_sum(40)[0]==(8,15,17)

# Problem 12
def num_divisors_sieve(n,proper=False):
    """Find the number of divisors for all nonnegative numbers less than `n'."""
    d = np.zeros(n,dtype=int)
    for i in range(1,n):
        d[i::i] += 1
    if proper and n>1:
        d[1:] += -1
    return d

assert(num_divisors_sieve(10) == [0,1,2,2,3,2,4,2,4,3]).all()
assert(num_divisors_sieve(10,True) == [0,0,1,1,2,1,3,1,3,2]).all()

# Problems 18, 67
def read_triangle(filename):
    """Read a triangular matrix from a file or string. Uses an array of arrays
    rather than 2d array because the inner arrays aren't uniform length.
    """
    with open(filename,"r") as file:
        tri = np.array(
            [np.array(
                 [int(n) for n in line.split()]
             ) for line in file]
        )
    return tri

# tri = read_triangle("./001/pe018.txt")
# assert tri[0][0] == 75
# assert(tri[1] == [95,64]).all()
# assert(tri[4] == [20,4,82,47,65]).all()

# Problems 18, 67
def max_sum_triangle(tri):
    """Find the maximum sum path in a binary tree. Requires tree in a matrix
    form. Uses an array of arrays rather than 2d array because the inner arrays
    aren't uniform length.
    """
    for i in range(len(tri)-1,0,-1):
        tri[i-1] += np.maximum(tri[i][1:],tri[i][:-1])
    return tri[0][0]

tri_test = [[3],[7,4],[2,4,6],[8,5,9,3]]
assert max_sum_triangle(tri_test) == 23

# Problems 21, 23
def sum_divisors_sieve(n,proper=True):
    """Sieve for the sum of proper divisors for natural numbers less than `n'.
    Optionally, we can include the number itself with `proper=False'."""
    dsum = np.ones(n,dtype=int)
    dsum[:2] = 0
    for i in range(2,int((n-1)**0.5)+1):
        dsum[i*i] += i
        dsum[i*(i+1)::i] += i + np.arange(i+1,(n-1)//i+1)
    if not proper:
        dsum += np.arange(0,n)
    return dsum

assert(sum_divisors_sieve(10,True ) == [0,0,1,1,3,1,6,1,7,4]).all()
assert(sum_divisors_sieve(10,False) == [0,1,3,4,7,6,12,8,15,13]).all()

# Problems 27,
def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    f = 5
    while f*f < n:
        if n%f == 0 or n%(f+2) == 0: return False
        f += 6
    return True
