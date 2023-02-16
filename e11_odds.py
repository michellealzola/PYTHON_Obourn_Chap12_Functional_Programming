def odds(num):
    odds = list(filter(lambda n: n % 2 != 0, range(num)))
    print(odds)


def main():
    number = 20
    odds(20)


if __name__ == '__main__':
    main()
