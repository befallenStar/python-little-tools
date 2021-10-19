# -*- encoding: utf-8 -*-
import json


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
        words = line.strip()
        word_json = json.loads(words)
        count[word_json['wordRank'] - 1] += 1
        headWord = word_json['headWord']
        content = word_json['content']['word']['content']
        if 'phone' in content.keys():
            phone = content['phone']
        elif 'ukphone' in content.keys():
            phone = content['ukphone']
        elif 'usphone' in content.keys():
            phone = content['usphone']
        else:
            phone = ''

        if 'speech' in content.keys():
            speech = content['speech']
        elif 'ukspeech' in content.keys():
            speech = content['ukspeech']
        elif 'usspeech' in content.keys():
            speech = content['usspeech']
        else:
            speech = ''

        phone = '/' + phone + '/'
        speech = 'https://dict.youdao.com/dictvoice?audio='+speech

        print(headWord)
        print(phone)
        print(speech)

if __name__ == '__main__':
    main()
