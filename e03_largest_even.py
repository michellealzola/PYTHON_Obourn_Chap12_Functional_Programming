def largest_even(seq):
    even_highest = max(filter(lambda x: x % 2 == 0, seq))
    return even_highest


def main():
    num_list = [5, -1, 12, 10, 2, 8]
    even_highest = largest_even(num_list)
    print(even_highest)


if __name__ == '__main__':
    main()
