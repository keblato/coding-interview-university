
def maxArea(height) -> int:
    i = 0
    j = len(height) - 1
    # Area = min(i,j) * j-r
    maxArea = 0
    while i < j:
        area = min(height[i], height[j]) * (j-i)
        maxArea = max(area, maxArea)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxArea


def main():
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == "__main__":
    main()
