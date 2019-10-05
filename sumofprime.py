# PROBLEM 10
# -----------
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# SOLUTION
# ---------
def is_prime(n):
	#runs as per O(1)
	#check if number if lesser or equal to one
    if n <= 1:
        return False
	#check if number is equal to two, return True since two is a prime
    if n == 2:
        return True
	#check if number is greater than two, that is start from three and check if number is even(even numbers cannot be prime)
    if n > 2 and n % 2 == 0:
        return False
 	#find the square root(**) of the number then find the whole number( int() ) of the square root
    max_sqrt = int(n**0.5)
	
	#loop through  the number and check if the number is divisible by another number
    for i in range(3, 1 + max_sqrt, 2):
        if n % i == 0:
            return False
	#return True if the number is prime
    return True


def is_prime(n):
	return n>=2 and all([n%i!=0 for i in range(2,1+int(n**.5))]) #the simplicity in list comprehension