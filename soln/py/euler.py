"""euler
This module provides common functions necessary to solve the Project Euler
problems.
"""

# Written by Steven Kuntz <stevenjkuntz@gmail.com>
# License: GNU

from functools import reduce
from math import log

from array import array
import numpy as np

# Problems 1, 6, 12
def triangular(n):
    """Find the ``n``th triangular number.

    ``T_n = 1 + 2 + ... + n``
    """
    return n*(n+1)//2

# Problems 3, 47
def prime_factors(n):
    """Find the prime factors of ``n``. Returns only primes, not their
    exponents.
    """
    p = []
    for f in [2, 3]:
        if n%f == 0:
            p += [f]
            while n%f == 0:
                n //= f
    f = 5
    while f*f < n:
        if n%f == 0:
            p += [f]
            while n%f == 0:
                n //= f
        f += 2 if f%6 > 1 else 4
    if n > 1:
        p += [n]
    return p


# Problem 4
def is_palindrome(n):
    """Check if an integer ``n`` is a palindrome by converting it to a string
    """
    n_str = str(n)
    return n_str == n_str[::-1]

# Problem 5
def lcm(a, b=None):
    """Find the least common multiple of a list of integers, recursively."""
    return reduce(lcm, a) if b is None else a*b//gcd(a, b)

# Problems 8
def gcd(a, b):
    """Find the greatest common divisor of two integers."""
    while b != 0:
        (a, b) = (b, a%b)
    return a

# Problems 5, 10, 26
def esieve(n):
    """Find all primes less than ``n`` with the Sieve of Eratosthenes."""
    if n <= 2:
        return array('l', [])

    isprime = array('b', [True]*(n//2))
    for k in range(3, int(n**0.5)+1, 2):
        if isprime[k//2]:
            for i in range(k*k//2, n//2, k):
                isprime[i] = False

    primes = array('l', [2])
    for i in range(1, n//2):
        if isprime[i]:
            primes.append(2*i+1)
    return primes


# Problem 7
def prime_bounds(n):
    """Find the lower and upper bounds of the ``n``th prime."""
    if n < 6:
        return [1, 14]
    lim = log(n)+log(log(n))
    return [int(n*(lim-1)), int(n*lim+1)]

# Problem 9, 39, 75
def pythagorean_triples_from_sum(s):
    """Find all Pythagorean triples ``a^2+b^2=c^2`` such that ``a+b+c=s`` and
    ``0<a<b<c<s``.
    """
    if s%2 == 1 or s < 12:
        return []
    trip = []
    for m in range(2, int((s/2)**0.5)+1):
        if (s//2)%m == 0:
            if m%2 == 0:
                k = m+1
            else:
                k = m+2
            while (k < 2*m) and k <= s/(2*m):
                if (s//(2*m))%k == 0 and gcd(m, k) == 1:
                    d = s//(2*k*m)
                    n = k - m
                    a = d*(m**2-n**2)
                    b = d*2*m*n
                    c = d*(m**2+n**2)
                    trip += [(min(a, b), max(a, b), c)]
                k += 2
    return trip

# Problem 12, 179
def num_divisors_sieve(n, proper=False):
    """Find the number of divisors for all nonnegative numbers less than ``n``.
    """
    d = np.zeros(n, dtype=int)
    for i in range(1, n//2):
        d[i::i] += 1
    if proper:
        d[1:n//2] += -1
    else:
        d[n//2:] += 1
    return d

# Problems 18, 67
def read_triangle(filename):
    """Read a triangular matrix from a file or string. Uses an array of arrays
    rather than 2d array because the inner arrays aren't uniform length.
    """
    with open(filename, "r") as file:
        tri = np.array(
            [np.array(
                [int(n) for n in line.split()]
            ) for line in file]
        )
    return tri

# Problems 18, 67
def max_sum_triangle(tri):
    """Find the maximum sum path in a binary tree. Requires tree in a matrix
    form. Uses an array of arrays rather than 2d array because the inner arrays
    aren't uniform length.
    """
    for i in range(len(tri)-1, 0, -1):
        tri[i-1] += np.maximum(tri[i][1:], tri[i][:-1])
    return tri[0][0]

# Problems 21, 23
def sum_divisors_sieve(n, proper=True):
    """Sieve for the sum of proper divisors for natural numbers less than ``n``.
    Optionally, we can include the number itself with ``proper=False``.
    """
    dsum = np.ones(n, dtype=int)
    dsum[:2] = 0
    for i in range(2, int((n-1)**0.5)+1):
        dsum[i*i] += i
        dsum[i*(i+1)::i] += i + np.arange(i+1, (n-1)//i+1)
    if not proper:
        dsum += np.arange(0, n)
    return dsum

# Problems 22, 42
def read_words(filename):
    """Read a list of words from file."""
    with open(filename) as file:
        words = []
        for line in file:
            words += line.replace("\"", "").split(",")
    return np.array(words)

# Problems 22, 42
def alphabetical_value(word):
    """Get the alphabetical value for a word or list of words."""
    if isinstance(word, str):
        word = [word]
    values = np.zeros(len(word), dtype=int)
    for i, word_i in enumerate(word):
        values[i] = sum([(ord(c)-64)%32 for c in word_i])
    return values

# Problems 27,
def is_prime(n):
    """Determine if a number ``n`` is prime."""
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    f = 5
    while f*f < n:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

# Problems 32, 38
def is_pandigital(n, digits=9):
    """Check if a number ``n`` is pandigital with respect to a set of
    ``digits``.
    """
    if isinstance(digits, int):
        digits = set(range(1, digits+1))
    n = [int(d) for d in str(n)]
    return len(n) == len(digits) and set(n) == digits

# Problems 44, 45
def pentagonal(n):
    """Find the ``n``th pentagonal number.

    ``P_n = n*(3*n+1)/2``
    """
    return n*(3*n-1)//2
