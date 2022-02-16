
def longestPalindrome(s: str) -> str:
    pal = ""
    lenPal = 0
    for i in range(0, len(s)):
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > lenPal:
                res = s[l:r+1]
                pal = res
                lenPal = (r-l+1)
            l -= 1
            r += 1
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > lenPal:
                res = s[l:r+1]
                pal = res
                lenPal = (r-l+1)
            l -= 1
            r += 1
    return pal


def main():
    print(longestPalindrome("babad"))


if __name__ == "__main__":
    main()
