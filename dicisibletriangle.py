# PROBLEM 12
# ----------
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# SOLUTION
# --------

n = input("Enter number: ")
def genfact(n):
    t = []
    for i in xrange(1, n+1):
        if n%i == 0:
            t.append(i)
    return t

print "Numbers of divisors: ", len(genfact(n))
print

m = input("Enter the number of triangle numbers to check: ")
print
for i in xrange (2, m+2):
    a = sum(xrange(i))
    b = len(genfact(a))
    if b > 500:
        print a