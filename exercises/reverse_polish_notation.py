from curses.ascii import isdigit
import math
from typing import List


def evalRPN(tokens: List[str]) -> int:
    # print(tokens)
    temp = tokens.pop()
    # print(temp)
    if temp.lstrip("-").isdigit():
        return temp
    else:
        val1 = evalRPN(tokens)
        val2 = evalRPN(tokens)
        res = eval(f'{val2} {temp} {val1}')
        if temp == "/":
            res = math.trunc(res)
        return (res)


def main():
    print(evalRPN(["10", "6", "9", "3", "+", "-11",
          "*", "/", "*", "17", "+", "5", "+"]))


if __name__ == "__main__":
    main()
