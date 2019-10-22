from stack import Stack1


"""
中缀表达式转换为后缀表达式
如：
    (a*b)+(c*d) -> ab*cd*+
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
            TopToken = opStack.pop()
            while TopToken != '(':
                postfixList.append(TopToken)
                TopToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and\
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


"""
中缀表达式转换为前缀表达式
如：
    (a*b)+(c*d) -> +*ab*cd
"""


def postfix(postfixExpr):
    postfixExpr = postfixExpr.upper()

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack1()
    postfixList = []
    for token in list(postfixExpr):
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM" or token in "1234567890":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topTaken = opStack.pop()
            while topTaken != '(':
                postfixList.insert(-2, topTaken)
                topTaken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and\
                    (prec[opStack.peek()] > prec[token]):
                postfixList.insert(-2, opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.insert(0, opStack.pop())

    return " ".join(postfixList)


if __name__ == "__main__":
    print(postfixEval("A+B*C+D*E+F"))
    print(postfixEval("(A+B)*C"))
    print(postfix("A+B*C+D*E+F"))
    print(postfix("(a*b)+(c*d)"))

    """
    A B C * + D E * + F +
    A B + C *
    + + + A * B C * D E F
    + * A B * C D
    """
