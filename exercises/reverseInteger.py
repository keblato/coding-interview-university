from xml.etree.ElementTree import tostring
import math


def reverse(x: int) -> int:
    esNeg = False
    if x < 0:
        esNeg = True
    x = abs(x)
    digits = 0
    if x > 0:
        digits = int(math.log10(x))+1
    elif x == 0:
        digits = 1
    i = digits - 1
    newNum = 0
    while i >= 0:
        k = x//10**i
        x -= k * 10**i
        newNum += k/10 * (10**(digits-i))
        i -= 1
    if(abs(newNum) > (2 ** 31 - 1)):
        return 0
    return int(newNum*-1) if esNeg else int(newNum)


def main():
    print(reverse(1534236469))


if __name__ == "__main__":
    main()
