# PROBLEM 16
# ----------
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

# SOLUTION
# --------
def sumOfDigit(num):
    sum_of_digits = 0
    while num > 9:
        sum_of_digits += num % 10
        num = num // 10  # use integer division // instead of /
    sum_of_digits += num
    return sum_of_digits

print(sumOfDigit(pow(2, 1000))) # use builtin pow or ** operator instead of math.pow