from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    table = {}
    for i in range(len(nums)):
        val = nums[i]
        if val in table:
            table[val].append(i)
        else:
            table[val] = [i]
    for j, k in table.items():
        print(j, k)
        if target - j in table:
            if target - j == j and len(k) > 1:
                return [k[0], k[1]]
            if target - j != j:
                return [k[0], table[target-j][0]]


def main():
    print(twoSum([2, 7, 11, 15, 7, 2], 4))


if __name__ == "__main__":
    main()
