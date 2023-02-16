from functools import reduce


def abs_sum(seq):
    absolute_sum = reduce(lambda a, b: abs(a) + abs(b), seq)
    return absolute_sum


def main():
    nums1 = [-1, 2, -4, 6, -9]
    absolute_sum = abs_sum(nums1)
    print(absolute_sum)


if __name__ == '__main__':
    main()
