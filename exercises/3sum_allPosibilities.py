from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:

    def twoSum(nums: List[int], target):
        # print(nums)
        res = []
        table = set()
        for i in range(len(nums)):
            v = nums[i]
            # print("vt", target-v in table)
            if i != 0 and target-v in table:
                res.append((v, target-v))
            table.add(v)
        return res
    nums.sort()
    res = set()
    for i, j in enumerate(nums):
        # Repito los numeros entonces no hacer como el two sums
        if i < len(nums)-2:
            for a in twoSum(nums[i+1:], -j):
                # print(a)
                res.add((j, a[0], a[1]))
    return res


def main():
    print(threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    main()
