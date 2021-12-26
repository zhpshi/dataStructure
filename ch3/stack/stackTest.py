class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] == '(':
            s.push('(')
        if symbolString[index] == ')':
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False

def matches(s1, s2):
    opens = '([{'
    closers = ')]}'
    if s1 in opens:
        return opens.index(s1) == closers.index(s2)
    else:
        return opens.index(s2) == closers.index(s1)

def parChecker_general(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] in "([{":
            s.push(symbolString[index])
        else:
            if symbolString[index] in ")]}":
                if s.isEmpty():
                    balanced = False
                else:
                    x = s.pop()
                    if not matches(x, symbolString[index]):
                        balanced = False
        index += 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False

def decimal2Binary(num):
    s = Stack()

    while num > 0:
        s.push(num % 2)
        num = num // 2
    binString  = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString

def baseConvert(num, base):
    s = Stack()
    digits = '0123456789ABCDEF'
    while num > 0:
        s.push(num % base)
        num = num // base
    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    return binString

def expressionConvert(expression):
    opstack = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    postfixlist = []
    tokenList = list(expression)
    s = list(expression)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOBQRSTUVWXYZ" or token in "1234567890":
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token  == ")":
            toptoken = opstack.pop()
            while toptoken != ')':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        else:
            while ( not opstack.isEmpty()) and prec[opstack.peek()] >= prec[token]:
                postfixlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1




def main():
    s1 = '((({)adx}))'
    print(parChecker_general(s1))
    print(baseConvert(25, 2))
    print(baseConvert(25, 16))



if __name__ == '__main__':
    main()