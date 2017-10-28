class Fraction:

	def __init__(self, top, bottom):
		self.num = top 
		self.den = bottom

	def show(self):
		print(self.num, '/', self.den)

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __add__(self, other):
		newnum = self.num * other.den + other.num * self.den 
		newden = self.den * other.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __eq__(self, other):
		firstnum = self.num * other.den 
		secondnum = self.den * other.num 
		return firstnum == secondnum



def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm % oldn

	return n 



x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
