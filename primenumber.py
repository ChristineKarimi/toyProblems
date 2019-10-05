# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime_number(limit):
	start = 2
	prime_list=[]
	while len(prime_list)<limit:
		for a in range(2,start):
			if start%a==0:
				continue
			else:
				prime_list.append(start)
				start+=1

		if len(prime_list)==limit:
			print(len(prime_list)-1)
			break

prime_number(6)