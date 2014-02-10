#coding=utf-8

import Queue as queue

class PerceptronModel(object):
    """This is an implemetion of Perceptron according "Statistic Learning Method"
    written by Li Hang"""
    def __init__(self, m=2):
        self.m = m
        self.w = [0 for i in range(m)]
        self.b = 0

    def set_w(self, w):
        self.w = w
        return None

    def set_b(self, b):
        self.b = b
        return None

    def train(self, T):
        iter_count = 0
        print "Iterate Count: %d, w: %s, b: %s" % (
            iter_count, self.w, self.b)
        while True:
            all_correct_classified = True
            iter_count += 1
            index = 0
            for index, (x, y) in enumerate(T):
                if not self.correct_classified(x, y):
                    self.w = [wi + yxi for (wi, yxi) in zip(self.w, (y * xi for xi in x))]
                    self.b = self.b + y
                    all_correct_classified = False
                    break
            index += 1
            if all_correct_classified:
                print "Iterate Count: %d, misclassification: None,  w: %s, b: %s" % (
                    iter_count, self.w, self.b)
                break
            print "Iterate Count: %d, misclassification: x[%d],  w: %s, b: %s" % (
                iter_count, index, self.w, self.b)
        return None

    def correct_classified(self, x, y):
        f = y * (sum(wi * xi for (wi, xi) in zip(self.w, x)) + self.b)
        if f > 0:
            return True
        return False

def main():
    p = PerceptronModel()
    T = [((3, 3), 1), ((4, 3), 1), ((1, 1), -1)]
    p.train(T)

if __name__ == '__main__':
    main()

