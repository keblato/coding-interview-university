from typing import List

from numpy import kron


def threeSumClosest(nums: List[int], target: int) -> int:
    res = nums[0] + nums[1] + nums[2]
    min = float("inf")
    # ordeno para saber si tengo que agregar negativos o positivos para quede menor
    nums.sort()
    for i in range(len(nums)-2):
        j, k = i + 1, len(nums)-1
        # Busco que target - (i,j,k) sea lo mas pequeña posible

        diff = target - nums[i]
        while(j < k):
            sum = diff - nums[j] - nums[k]
            absSum = abs(sum)
            if absSum < min:
                min = absSum
                res = target-sum
            if absSum == 0:
                return res
            # Si es muy grande entonces agrego numeros mas pequeños, sino agrego grandes
            elif sum > 0:
                j += 1
            else:
                k -= 1
    return res


def main():
    print(threeSumClosest([-3, -2, -5, 3, -4], -1))
    # -3 -2 + 3
    # 0,1,3


if __name__ == "__main__":
    main()
