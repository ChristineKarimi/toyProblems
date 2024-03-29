# PROBLEM 35
# ---------
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

# SOLUTION
# --------
def circular_prime(limit = 100000):
    count = 0
    prime_set = set(get_primes(limit))
    for r in prime_set:
        num = str(r)
        if all(int(num[i:]+num[:i]) in prime_set for i in xrange(len(num))):
            count += 1
    return count