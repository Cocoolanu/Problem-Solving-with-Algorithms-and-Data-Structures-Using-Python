from stack import Stack

def binaryConvert(num):
    myStack = Stack()
    binaryString = ''
    while num > 0:
        temp = num % 2
        myStack.push(temp)
        num = num // 2

    while not myStack.isEmpty():
        binaryString += str(myStack.pop())

    return binaryString

print(binaryConvert(17))
print(binaryConvert(45))
print(binaryConvert(96))
