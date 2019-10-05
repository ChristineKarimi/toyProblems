# PROBLEM 6
# ------------
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# SOLUTION
# ----------
def sum_of_square(limit):
    my_list = []
    start = 1
    while start<=limit:
        square = start*start
        my_list.append(square)
        start+=1
        p = sum(my_list)
        if len(my_list)==limit:
            m = sum(my_list)
    return m