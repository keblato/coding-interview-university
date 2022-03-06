from typing import List


def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    # Que necesito para que los nuevos pesos den igual

    for box in aliceSizes:
        # sumaA - box == sumaB + box
        necesito = box + (sumB-sumA)//2
        if necesito in bobSizes:
            return [box, necesito]


def main():
    print(fairCandySwap([2], [1, 3]))


if __name__ == "__main__":
    main()
