class Fraction:

	def __init__(self, top, bottom):
		if type(top) is not int or type(bottom) is not int:
			raise ValueError("Please only use integers")
		else:
			common = gcd(top, bottom)
			self.num = top // common
			self.den = bottom // common

	def show(self):
		print(self.num, '/', self.den)

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __add__(self, other):
		newnum = self.num * other.den + other.num * self.den 
		newden = self.den * other.den
		#common = gcd(newnum, newden)
		#return Fraction(newnum // common, newden // common)
		return Fraction(newnum, newden)

	def __sub__(self, other):
		newnum = self.num * other.den - other.num * self.den 
		newden = self.den * other.den
		return Fraction(newnum, newden)

	def __mul__(self, other):
		return Fraction(self.num * other.num, self.den * other.den)

	def __truediv__(self, other):
		newnum = self.num * other.den 
		newden = self.den * other.num
		return newnum / newden

	def __eq__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum == secondnum

	def __gt__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum > secondnum		

	def __ge__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum >= secondnum	

	def __lt__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum < secondnum	

	def __le__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum <= secondnum

	def __ne__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum != secondnum		

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den



def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm % oldn

	return n 


#z = Fraction(1.5, 2.3)
x = Fraction(1,2)
y = Fraction(2,3)
print("{0} grater than {1}? {2}".format(x, y, x > y))
print("{0} grater or equal to {1}? {2}".format(x, y, x >= y))
print("{0} less than {1}? {2}".format(x, y, x < y))
print("{0} less or equal to {1}? {2}".format(x, y, x <= y))
print("{0} not equal to {1}? {2}".format(x, y, x != y))
print("sum is:", x+y)
print("true divsion is:", x/y)
print("difference is:", x-y)
print("product is:", x*y)
print("equality is:", x == y)
print("numerator is:", x.getNum())
print("denominator is:", x.getDen())
