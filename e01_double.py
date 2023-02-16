def double(seq):
    double_list = list(map(lambda x: x * 2, seq))
    return double_list


def main():
    nums1 = [2, -1, 4, 16]
    double_list = double(nums1)
    print(double_list)


if __name__ == '__main__':
    main()
