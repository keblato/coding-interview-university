def myAtoi(s: str) -> int:
    res = ""
    esPos = True
    signusFind = False
    encontreNum = False
    for c in s:
        if c == " ":
            if encontreNum or signusFind:
                break
            continue
        elif c == '-':
            if signusFind or encontreNum:
                break
            esPos = False
            signusFind = True
            continue
        elif c == '+':
            if signusFind or encontreNum:
                break
            esPos = True
            signusFind = True
            continue
        try:
            int(c)
            encontreNum = True
            res += c
        except ValueError:
            break
    res = 0 if len(res) == 0 else int(res) if esPos else int(res)*-1
    if(res > (2 ** 31 - 1)):
        return 2 ** 31 - 1
    elif (res < -(2 ** 31)):
        return -(2 ** 31)

    return res


def main():
    print(myAtoi("00000-42a1234"))


if __name__ == "__main__":
    main()
