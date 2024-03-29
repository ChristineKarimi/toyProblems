# PROBLEM 20
# ----------
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# SOLUTION
# --------
import time
 
def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
 
def sum_digits(n):
    return sum([int(i) for i in str(n)])
 
start = time.time()
 
sumfac = sum_digits(factorial(100))
 
elapsed = time.time() - start
 
print("%s found in %s seconds") % (sumfac,elapsed)
