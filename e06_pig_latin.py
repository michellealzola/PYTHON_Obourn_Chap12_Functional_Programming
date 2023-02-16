def pig_latin(sentence):
    sentence_clean = sentence.split()
    strings = []
    for word in sentence_clean:
        strings.append(word)
    translation = list(map(lambda s: s[1:len(s)] + '-' + s[0] + 'ay', strings))
    for word in translation:
        print(word, end=' ')


def main():
    sentence = 'go seattle mariners'
    pig_latin(sentence)


if __name__ == '__main__':
    main()
