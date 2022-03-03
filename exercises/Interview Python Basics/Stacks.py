from collections import deque
from opcode import stack_effect


from numpy import empty


def evaluate_postfix_expression(s: str):
    stack = deque()
    for i in s:
        if i.isdigit():
            stack.append(i)
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(str(eval(b + i + a)))

    return stack[0]


def insertBotton(nD: deque, top):
    if len(nD) == 0:
        nD.append(top)
    else:
        temp = nD.pop()
        insertBotton(nD, top)
        nD.append(temp)


def reverse_stack_recursion(d: deque):
    if len(d) > 0:
        temp = d.pop()
        reverse_stack_recursion(d)
        insertBotton(d, temp)


def sort_values_stack_recursion(d: deque):
    if len(d) > 0:
        temp = d.pop()
        sort_values_stack_recursion(d)
        sorted_insert(d, temp)


def sorted_insert(d: deque, elem):
    if len(d) == 0:
        d.append(elem)
    else:
        top = d.pop()
        d.append(top)
        if elem > top:
            d.append(elem)
        else:
            temp = d.pop()
            sorted_insert(d, elem)
            d.append(temp)


def check_balanced_brackets(s: str):
    print(s)
    brackets = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    dCheck = deque()
    for i in s:
        if i in brackets:
            dCheck.append(i)
        else:
            if len(dCheck) > 0:
                temp = dCheck.pop()
                if brackets[temp] != i:
                    return False
            else:
                return False

    return True


def main():
    # print(evaluate_postfix_expression("231*+9-"))

    # reverse = deque(["1", "2", "3"])
    # print(reverse)
    # reverse_stack_recursion(reverse)
    # print(reverse)

    # toSort = deque([1, 3, 2, 7, 5])
    # print(toSort)
    # print(sort_values_stack_recursion(toSort))
    # print(toSort)

    print(check_balanced_brackets("[(])"))


if __name__ == "__main__":
    main()
