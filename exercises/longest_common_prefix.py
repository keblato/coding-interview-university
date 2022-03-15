from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    encontro = True
    i = 0
    res = ""
    while(encontro):
        actual = ""
        for k in strs:
            # print(res)
            if i < len(k):
                if actual == "":
                    actual = k[i]
                if actual != k[i]:
                    return res
            else:
                return res
        res += actual
        i += 1


def main():
    print(longestCommonPrefix(["flow", "flow", "flower"]))


if __name__ == "__main__":
    main()
