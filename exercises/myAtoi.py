def myAtoi(s: str) -> int:
    res = 0
    esPos = True
    for c in s:
        print(type(c))
        if c == " ":
            continue
        if type(c) == type(s):
            if c == '-':
                esPos = False
                continue
            elif c == '+':
                esPos = True
            return res
    return 0


def main():
    print(myAtoi('-123 asd'))


if __name__ == "__main__":
    main()
