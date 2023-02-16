import math


def total_circle_area(seq):
    total_area = sum(map(lambda x: math.pi * (x**2), seq))
    return total_area


def main():
    radii = [3.0, 1.0, 7.2, 5.5]
    total_area = total_circle_area(radii)
    print(f'{total_area:.0f}')


if __name__ == '__main__':
    main()
