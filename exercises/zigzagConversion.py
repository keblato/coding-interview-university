def convert(s: str, numRows: int) -> str:
    i = 0
    j = 0
    matrix = [""]*numRows
    direction = True  # True down
    if numRows == 1:
        return s
    while j < len(s):
        matrix[i] += s[j]
        if i == numRows - 1:
            direction = False
        if i == 0:
            direction = True
        if direction:
            i += 1
        else:
            i -= 1
        j += 1

    return ''.join(matrix)


def main():
    print(convert("Asdasd", 1))


if __name__ == "__main__":
    main()
