from logging.config import valid_ident


def isMatch(s: str, p: str) -> bool:
    i = 0
    j = 0
    validV = p[0]
    oneTime = True
    if j+1 < len(p):
        if p[j+1] == '*':
            j += 1
            oneTime = False

    # j always in
    # Al finalizar siempre dejo j fuera de la lista
    while(i < len(s) or j < len(p)):

    return True


def main():
    print(isMatch(
        "a",
        "a*b*c*d*"))


if __name__ == "__main__":
    main()
