import random
from typing import List


def shuffleDeck(deck):
    res = []
    n = len(deck)
    while n > 0:
        randonPos = random.randint(0, len(deck)-1)
        res.append(deck.pop(randonPos))
        n -= 1
    return res


def iterativeVowelsWeight(s, vowelsW):
    res = 0
    for i in s:
        if i in vowelsW:
            res += vowelsW[i]
    return res


def recursiveVowelsWeight(s, vowelsW) -> int:
    letter = s[0]
    newString = s[1:len(s)]
    val = vowelsW[letter] if letter in vowelsW else 0
    if len(newString) > 0:
        val += recursiveVowelsWeight(newString, vowelsW)
    return val


def matchRegex(word):
    import re
    subW = ["odoo"]
    res = [word for ele in test_list if(ele in test_string)]
    regexp = re.compile(r'[a-zA-Z]{4,9}')
    if regexp.match(word):
        print('matched')


def main():
    # print("asdasd"[1:2])
    # print(shuffleDeck(['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']))
    # print(iterativeVowelsWeight("Welcome to Indonesia", {
    #     "a": 1, "e": 2, "i": 3, "o": 4, "u": 5
    # }))

    print(matchRegex("asdasdasdasd"))


if __name__ == "__main__":
    main()
