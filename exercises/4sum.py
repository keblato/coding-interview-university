from typing import List

from numpy import kaiser


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []
        a_value = target // k
        if not nums:
            return res
        if nums[0] > a_value or nums[-1] < a_value:
            return res

        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                # si no hay nada no lo recorro ?
                for sub in kSum(nums[i+1:], target - nums[i], k-1):
                    res.append([nums[i]] + sub)
        return res

    def twoSum(nums: List[int], target):
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
    nums.sort()
    return kSum(nums, target, 4)


def main():
    print(fourSum([1, 0, -1, 0, -2, 2], 0))


if __name__ == "__main__":
    print([1] + [12, 3])
    main()
