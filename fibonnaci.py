class Fibonnaci(object):

    def __init__(self, threshold):
        self.threshold = threshold
        self.first = self.second = 0

    def __iter__(self):
        return self

    def next(self):
        if self.first != 0:
            tmp_first = self.first
            self.first = self.first + self.second
            self.second = tmp_first
        else:
            self.first = 1

        if self.first >= self.threshold:
            raise StopIteration

        return self.first


if __name__ == '__main__':
    for fibo_num in Fibonnaci(130):
        print fibo_num
