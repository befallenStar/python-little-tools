# -*- encoding: utf-8 -*-
import json
from word import Word


def replaceFran(str):
    fr_en = [['é', 'e'], ['ê', 'e'], ['è', 'e'], ['ë', 'e'], ['à', 'a'],
             ['â', 'a'], ['ç', 'c'], ['î', 'i'], ['ï', 'i'], ['ô', 'o'],
             ['ù', 'u'], ['û', 'u'], ['ü', 'u'], ['ÿ', 'y']]
    for i in fr_en:
        str = str.replace(i[0], i[1])
    return str


def main():
    with open('Level4luan_2.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = [0] * len(lines)
    for line in lines:
        word_json = line.strip()
        word = Word(word_json)
        print(word)


if __name__ == '__main__':
    main()
