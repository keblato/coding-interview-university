def lengthOfLongestSubstring(self, s: str) -> int:
    dictWords = {}
    res = 0
    tempRes = 0
    i = 0
    l = 0
    while i < len(s):
        x = s[i]
        if x not in dictWords:
            dictWords[x] = i
            tempRes += 1
        else:
            i = dictWords[x]
            dictWords = {}
            if tempRes > res:
                res = tempRes
            tempRes = 0
        i += 1
        l += 1
       # print(i)
       # print(dictWords)
    if tempRes > res:
        res = tempRes
    # print(res)
    # print(dictWords)
    return res


def main():
    lengthOfLongestSubstring("a", "")


if __name__ == "__main__":
    main()
