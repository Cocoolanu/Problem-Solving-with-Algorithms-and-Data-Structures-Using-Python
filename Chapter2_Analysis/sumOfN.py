import time

def sumOfN(n):
	start = time.time()

	theSum = 0
	for i in range(1, n+1):
		theSum += i

	end = time.time()

	return theSum, end-start


for i in range(5):
	print("Sum is %d required %10.7f seconds" % sumOfN(1000000))


def sumOfN3(n):
	start = time.time()
	sum_n = (n*(n+1))/2
	end = time.time()

	return sum_n, end-start

print()

for i in range(5):
	print("Sum is %d required %10.7f seconds" % sumOfN3(10000))

