"""
题目内容：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
输入格式:
    一行字符串
输出格式：
    True或False，表示该输入是否为合法括号串
输入样例：
    ([])
输出样例：
    True
"""


def isValid(s):
    if s == '':
        return True
    balanced = False
    s = list(s)
    if len(s) % 2 != 0:
        return False
    lis = []
    if (s[0] != ')' and s[0] != '}' and s[0] != ']') and not balanced:
        for symbol in s:
            if symbol in "[({":
                lis.append(symbol)
            elif symbol in ")]}":
                if symbol == ")" and lis.pop() == "(":
                    balanced = True
                if symbol == "]" and lis.pop() == "[":
                    balanced = True
                if symbol == "}" and lis.pop() == "{":
                    balanced = True
    return balanced


# print(isValid(input()))


"""
题目内容：
根据每日气温列表，请重新生成一个列表，对应位置的输入是你需要再等
待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替
输入格式:
    一行以Python表达式格式给出的列表，包含数个整数
输出格式：
    整数组成的列表，直接使用print输出
输入样例：
    [73, 74, 75, 71, 69, 72, 76, 73]
输出样例：
    [1, 1, 4, 2, 1, 1, 0, 0]
"""


def dailyTemp(T):
    lis = [0]*len(T)
    for day in range(len(T)):
        for date in range(day, len(T)):
            if T[day] < T[date]:
                lis[day] = date-day
                break
    return lis
# t = eval(input())
# print(dailyTemp(t))


"""
题目内容：
    根据后缀表达式表示法，求表达式的值。
    有效的运算符包括 + , -, *, / ；其中除法仅保留整数结果。
    若出现除数为0或表达式非法的情况，输出"NaN"
注：
    每个数字token可包含多位，也可为负数
    除法统一使用 int(a / b) 而非 a // b 进行计算
输入格式:
    一行字符串，每个token间以空格分隔
输出格式：
    一行，包含一个整数或"NaN"
输入样例：
    "4 13 5 / +"
输出样例：
    6
"""


def calc(tokens):
    stack = []
    result = 0
    for token in tokens:
        if token in "+-*/":
            try:
                stack.append(math_cal(int(stack.pop()), int(stack.pop()),token))
            except IndexError:
                return "NaN"
        else:
            stack.append(token)
        if stack[-1] == "NaN":
            return "NaN"
    return stack[0]


def math_cal(part1, part2, operation):
    if operation == "+":
        return part1 + part2
    elif operation == "-":
        return part2 - part1
    elif operation == "*":
        return part1 * part2
    elif operation == "/":
        if part1 == 0:
            return "NaN"
        else:
            return int(part2 / part1)


# print(calc(input().split()))
