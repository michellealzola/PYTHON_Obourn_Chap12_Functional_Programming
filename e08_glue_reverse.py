from functools import reduce


def glue_reverse(seq):
    reverse_list = reduce(lambda a, b: str(a) + str(b), reversed(seq))
    print(reverse_list)


def main():
    word_list = ["the", "quick", "brown", "fox"]
    glue_reverse(word_list)


if __name__ == '__main__':
    main()
