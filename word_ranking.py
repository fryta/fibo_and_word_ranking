class WordRanking(object):

    def __init__(self, sentence):
        self.sentence = sentence
        self.ranking = self._generate_ranking()

        self._sort_ranking()

    def _generate_ranking(self):
        ranking = {}

        for word in self.sentence.split():
            try:
                ranking[word] += 1
            except KeyError:
                ranking[word] = 1

        return [(word, freq) for word, freq in ranking.iteritems()]

    def _sort_ranking(self):
        self.ranking = sorted(self.ranking, key=lambda item: item[1], reverse=True)

    def get_ranking(self):
        return self.ranking


if __name__ == '__main__':
    word_ranking = WordRanking('to jest test test test ala ala')
    print word_ranking.get_ranking()
