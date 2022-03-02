def isPalindrome(x: int) -> bool:
    # is number
    if x < 0:
        return False
    sx = str(x)
    if len(sx) == 2:
        if sx[0] == sx[1]:
            return True
        else:
            return False

    i = len(sx)//2
    j = i
    esPaliEven = True
    while i >= 0 and j < len(sx) and esPaliEven and len(sx) % 2 != 0:
        if sx[i] == sx[j]:
            i -= 1
            j += 1
        else:
            esPaliEven = False

    i = len(sx)//2 - 1
    j = i+1
    esPaliOdd = True

    while i >= 0 and j < len(sx) and esPaliOdd and len(sx) % 2 == 0:
        if sx[i] == sx[j]:
            i -= 1
            j += 1
        else:
            esPaliOdd = False
    if esPaliEven and esPaliOdd:
        return True
    return False


def main():
    print(isPalindrome(100))


if __name__ == "__main__":
    main()
