from stack import Stack1


def parChecker(symbolString):
    s = Stack1()
    balanced = True
    index = 0
    # 如果括号匹配，左右括号数目相等，压入的括号都会弹出来，不会出现残留问题或者balance为False的问题
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1
    
    if balanced and s.isEmpty():    # 防止两种情况，左括号多余有括号或者有括号多余左括号
        return True
    else:
        return False


if __name__ == "__main__":
    print(parChecker("((((((((()))))))))"))
    print(parChecker("(((((()))))"))
