import json

class Mood:
    def __init__(self) -> None:
        self.score = 0
    
    def count_mood(self, words_in_diary):
        list_of_words = self.split_text(words_in_diary)
        try:
            self.score = self.calculate_mood(list_of_words)
            return self.score
        except IndexError:
            pass
        # print(self.score)

    def split_text(self, words_in_diary):
        punctuations = '''.?!-~,"':/()<>'''
        no_punctuations = ""

        for char in words_in_diary:
            if char not in punctuations:
                no_punctuations += char
        list_of_words = no_punctuations.split()
        return list_of_words

    def calculate_mood(self, list_of_words):
        score = 0
        with open("hariku/keywords.json",) as json_keywords:
            keywords = json.load(json_keywords)
            for word in list_of_words:
                if word in keywords['positive']:
                    score += 1
                elif word in keywords['negative']:
                    score -= 1
        return score

