# -*- encoding: utf-8 -*-
import json


class Word:
    def __init__(self, word_json):
        word = json.loads(word_json)
        self.head_word = word['headWord']
        self.content = word['content']['word']['content']

        self.phone = ''
        if 'phone' in self.content.keys():
            self.phone = self.content['phone']
        elif 'ukphone' in self.content.keys():
            self.phone = self.content['ukphone']
        elif 'usphone' in self.content.keys():
            self.phone = self.content['usphone']

        self.speech = ''
        if 'speech' in self.content.keys():
            self.speech = self.content['speech']
        elif 'ukspeech' in self.content.keys():
            self.speech = self.content['ukspeech']
        elif 'usspeech' in self.content.keys():
            self.speech = self.content['usspeech']

        if '/' not in self.phone:
            self.phone = '/' + self.phone + '/'
        self.speech = 'https://dict.youdao.com/dictvoice?audio=' + self.speech

        self.trans = self.content['trans']

        self.phrases = []
        if 'phrase' in self.content.keys():
            self.phrases = self.content['phrase']['phrases']

        self.sentences = []
        if 'sentence' in self.content.keys():
            self.sentences = self.content['sentence']['sentences']

    def __str__(self):
        word = self.head_word + '\t' + self.phone + '\t' + self.speech
        for t in self.trans:
            word += '\n' + t['pos'] + '.\t' + t['tranCn']
            if 'tranOther' in t.keys():
                word += '\t' + t['tranOther']
        for p in self.phrases:
            word += '\n' + p['pContent'] + '\t' + p['pCn']
        for s in self.sentences:
            word += '\n' + s['sContent'] + '\n' + s['sCn']
        return word
