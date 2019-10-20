from stack import Stack1


"""
中缀表达式转换为前缀表达式
如：
    (a*b)+(c*d) -> +*ab*cd
"""


def postfixEval(postfixExpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack1()
    postfixList = []
    tokenList = list(postfixExpr)
    for token in tokenList:
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM" or token in "1234567890":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            x = opStack.peek()
            print(x)
            while (not opStack.isEmpty()) and \
                (x >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == "__main__":
    print(postfixEval("A+B*C"))
