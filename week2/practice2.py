from stack import Stack1

"""
十进制与二进制的转换
"""


def divideBy2(decNumber):
    remstack = Stack1()

    while decNumber > 0:
        rem = decNumber % 2     # 整数取余
        remstack.push(rem)
        decNumber = decNumber//2

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString


def BaseConverter(decNumber, base):
    remstack = Stack1()

    while decNumber > 0:
        rem = decNumber % base    # 整数取余
        remstack.push(rem)
        decNumber = decNumber//base

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString


if __name__ == "__main__":
    print(divideBy2(42))
    print(BaseConverter(42, 8))
