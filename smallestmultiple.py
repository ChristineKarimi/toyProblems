# PROBLEM 5
# ---------
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# SOLUTION
# ---------
def smallest_m(limit):
    start = 1
    while True:
        if all(start % i == 0 for i in range(limit, 1,-1)):
            return start
            break
        else:
            start+=1

smallest_m(20)