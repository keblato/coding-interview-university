from typing import List
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    """if not ((len(nums1) + len(nums2)) % 2 == 0):
        findMedianSortedArrays(self, nums1=nums1, nums2=nums2, odd=True)
     """
    numberToMake: int = decimal.Decimal(
        (len(nums1) + len(nums2))/2).to_integral_value() - 1
    n = len(nums1)
    m = len(nums2)
    
    print(numberToMake)
    return 0.0


def whenOdd(elemnts):
    return decimal.Decimal(len(elemnts)/2).to_integral_value()-1


"""  
    a-> n-1 and b-> n+1
"""


def whenEven(elements):
    print(decimal.Decimal((len(elements)+1)/2).to_integral_value()-1)
    print(decimal.Decimal((len(elements)-1)/2).to_integral_value()-1)


def main():
    findMedianSortedArrays("a", [1, 3, 4], [1, 2])


if __name__ == "__main__":
    main()
