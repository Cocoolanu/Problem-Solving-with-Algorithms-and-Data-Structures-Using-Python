class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



def revstring(mystr):
	myStack = Stack()
	newStr = ''
	for ch in mystr:
		myStack.push(ch)

	while not myStack.isEmpty():
		newStr += myStack.pop()

	return newStr

'''
s = Stack()
print(revstring("1234567890"))

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
'''
