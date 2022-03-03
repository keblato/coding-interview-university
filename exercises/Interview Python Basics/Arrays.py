import sys


def find_second_minimum(ls) -> int:
    res = [float("inf"), float("inf")]
    for e in ls:
        if e < res[0]:
            res[1] = res[0]
            res[0] = e
        elif e < res[1]:
            res[1] = e

    return res

# el primer numero que no se repite


def first_non_repeating_integers(ls):
    help = {}
    res = None
    i = 0
    j = len(ls) - 1
    for e in ls:
        if e not in help:
            help[e] = 1
        else:
            help[e] += 1
    for h, v in help.items():
        if v == 1:
            return h
    return None


def merge_two_sorted_arrays(ls1, ls2):
    i = 0
    j = 0
    k = 0
    res = []
    while(i+j < len(ls1) + len(ls2)):
        if i >= len(ls1):
            res.append(ls2[j])
            j += 1
        elif j >= len(ls2):
            res.append(ls1[i])
            i += 1
        elif ls1[i] < ls2[j]:
            res.append(ls1[i])
            i += 1
        else:
            res.append(ls2[j])
            j += 1
        k += 1

    return res


def rearrange_positive_and_negative_values(ls):
    n = len(ls)
    i = -1
    for j in range(n):
        if ls[j] < 0:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    print(ls,)
    print("----", i)
    j = 0
    i += 1
    pos = False
    while j < i and i < len(ls):
        print(i, j)
        if ls[i] > ls[j] and pos:
            ls[j], ls[i] = ls[i], ls[j]
            pos = False
            i += 1
            j += 1
        else:
            pos = True
            j += 1
    print(ls)


def main():
    # print(find_second_minimum([-2, 1, 5, 3, -1, 4, 2, 6]))
    # print(first_non_repeating_integers([1, 1, 3, 4, 5, 3, 4, 6]))
    # print(merge_two_sorted_arrays([1, 2, 3, 3, 3, 5], [2, 3, 4, 5]))
    print(rearrange_positive_and_negative_values(
        [-1, 2, -3, 4, 5, 6, -7, 8, 9]))
    pass


if __name__ == "__main__":
    main()
