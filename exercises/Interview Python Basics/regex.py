import re


def checkEmail(s):
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
    if (re.search(pattern, s)):
        return "Valid email"
    else:
        return "Invalid email"


def main():
    print(checkEmail("keblato1@gmail1.com"))


if __name__ == "__main__":
    main()
