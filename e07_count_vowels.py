def count_vowels(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = filter(lambda s: s.lower() in vowels, sentence)
    for vowel in vowel_list:
        count += 1
    return count


def main():
    sentence = 'SOO beautiful'
    vowel_count = count_vowels(sentence)
    print(vowel_count)


if __name__ == '__main__':
    main()
