# PROBLEM 9
# ---------
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# SOLUTION
# --------
def triplet(total):
	start=2
	for x in range(1,start):
		y=x+1
		z=y+1
		summation = x+y+z
		while summation<=total:
			while z * z < x * x + y * y:
				z +=1

			if z * z == x * x + y * y:
				mult = x*y*z

		return mult

triplet(12)