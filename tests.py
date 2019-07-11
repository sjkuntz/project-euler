from euler import *

assert triangular(1) == 1
assert triangular(2) == 3
assert triangular(100) == 5050

assert prime_factors(2) == [2]
assert prime_factors(3) == [3]
assert prime_factors(4) == [2]
assert prime_factors(5) == [5]
assert prime_factors(6) == [2, 3]
assert prime_factors(24) == [2, 3]

assert is_palindrome(9009)

assert esieve(2).size == 0
assert esieve(3) == [2]
assert(esieve(10) == [2, 3, 5, 7]).all()
assert(esieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]).all()

assert prime_bounds(4) == [1, 14]
assert prime_bounds(6) == [8, 15]
assert prime_bounds(10) == [21, 32]

assert pythagorean_triples_from_sum(12)[0] == (3, 4, 5)
assert pythagorean_triples_from_sum(40)[0] == (8, 15, 17)

assert(num_divisors_sieve(10) == [0, 1, 2, 2, 3, 2, 4, 2, 4, 3]).all()
assert(num_divisors_sieve(10, True) == [0, 0, 1, 1, 2, 1, 3, 1, 3, 2]).all()

TRI = read_triangle("./001/pe018.txt")
print(TRI)
assert TRI[0][0] == 75
assert(TRI[1] == [95, 64]).all()
assert(TRI[4] == [20, 4, 82, 47, 65]).all()

TRI_TEST = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
assert max_sum_triangle(TRI_TEST) == 23

assert(sum_divisors_sieve(10, True) == [0, 0, 1, 1, 3, 1, 6, 1, 7, 4]).all()
assert(sum_divisors_sieve(10, False) == [0, 1, 3, 4, 7, 6, 12, 8, 15, 13]).all()

assert alphabetical_value("Bob") == 19
assert (alphabetical_value(["Bob", "Alice"]) == [19, 30]).all()

D = {1, 2, 3, 4}
assert is_pandigital(1234, D)
assert is_pandigital(4321, D)
assert not is_pandigital(1235, D)
assert not is_pandigital(1233, D)
assert not is_pandigital(12334, D)

assert pentagonal(1) == 1
assert pentagonal(2) == 5
assert pentagonal(10) == 145
