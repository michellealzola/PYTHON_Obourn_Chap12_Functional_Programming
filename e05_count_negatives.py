def count_negatives(seq):
    neg_count = len(list(filter(lambda x: x < 0, seq)))
    return neg_count


def main():
    num_list = [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6]
    neg_count = count_negatives(num_list)
    print(neg_count)


if __name__ == '__main__':
    main()
