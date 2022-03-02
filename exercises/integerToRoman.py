import math


def intToRoman(num: int) -> str:
    numConv = {
        5: "V",
        50: "L",
        500: "D",
    }
    firstNum = {
        0: "I",
        1: "X",
        2: "C",
        3: "M"
    }
    secondNum = {
        4: {
            0: "IV",  # 4
            1: "XL",  # 40
            2: "CD",  # 400
        },
        9: {
            0: "IX",  # 9
            1: "XC",  # 90
            2: "CM",  # 900
        }
    }
    s = str(num)
    i = 0
    res = ""
    if num < 10:

        dig = num
        if dig == 4:
            res += secondNum[4][i]
        elif dig == 9:
            res += secondNum[9][i]
        else:
            if dig >= 5:
                dig -= 5
                res += numConv[5*10**i]
            res += firstNum[i]*dig
    else:
        for i in range(math.ceil(math.log(num, 10))-1, -1, -1):
            dig = ((num//(10**i)) % 10)
            print("------------- I ", i, " ---- DIG ", dig)
            if dig == 4:
                res += secondNum[4][i]
            elif dig == 9:
                res += secondNum[9][i]
            else:
                if dig >= 5:
                    dig -= 5
                    res += numConv[5*10**i]
                res += firstNum[i]*dig
    return res
# Problema con los 1, 10 ,100


def main():
    print(intToRoman(10))


if __name__ == "__main__":
    main()
