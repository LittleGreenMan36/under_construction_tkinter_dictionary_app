import json

def open_data_file(word):
    with open('data/D{}.json'.format(word[0])) as file:
        return json.loads(file.read())

class Word:
    def __init__(self, word):
        self.word = word

    def get_info(self):
        keys = []   
        data = open_data_file(self.word)
        for word in data:
            key = list(data[word]['MEANINGS'])

            if not key: 
                key = '0'
                keys.append(key)
                continue

            else: 
                keys.append(key)

        meanings = []
        word_position = list(data.keys()).index(self.word)

        if keys[word_position] == '0':
            print('No Meanings')
            quit()

        for idx, item in enumerate(keys[word_position]):
            meaning = data[self.word]['MEANINGS'][item][1]       
                 
            if len(keys[list(data.keys()).index(self.word)]) == 0:
                return [meaning]

            else:
                meanings.append(meaning)
                if idx == len(keys[word_position]) - 1: 
                    return [meanings, data[self.word]['SYNONYMS'], data[self.word]['ANTONYMS']]