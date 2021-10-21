# -*- encoding: utf-8 -*-
import json


class Word:
    def __init__(self, word_json):
        word = json.loads(word_json)
        self.head_word = word['headWord']
        self.content = word['content']['word']['content']
        if 'phone' in self.content.keys():
            self.phone = self.content['phone']
        elif 'ukphone' in self.content.keys():
            self.phone = self.content['ukphone']
        elif 'usphone' in self.content.keys():
            self.phone = self.content['usphone']
        else:
            self.phone = ''

        if 'speech' in self.content.keys():
            self.speech = self.content['speech']
        elif 'ukspeech' in self.content.keys():
            self.speech = self.content['ukspeech']
        elif 'usspeech' in self.content.keys():
            self.speech = self.content['usspeech']
        else:
            self.speech = ''

        self.phone = '/' + self.phone + '/'
        self.speech = 'https://dict.youdao.com/dictvoice?audio='+self.speech

    def __str__(self):
        return self.head_word + '\t' + self.phone + '\t' + self.speech