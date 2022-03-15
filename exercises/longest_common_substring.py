from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    return recRes(strs.pop(), strs) or ""


def recRes(word: str, strs: List[str]):
    encontro = True
    for k in strs:
        if word not in k:
            encontro = False
            break
    if encontro:
        return word
    else:
        val1 = recRes(word[1:], strs)
        val2 = recRes(word[:len(word)-1], strs)
        return val1 if len(val1) > len(val2) else val2


def main():
    print(longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    main()
