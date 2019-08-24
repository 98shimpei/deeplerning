# coding: utf-8

import numpy as np
class Perceptron:
    def __init__(self, weights, threashold):
        self.weights = weights
        self.threashold = threashold

    def output(self, input_data):
        if len(input_data) != len(self.weights):
            print("入力数が違います")
            raise IndexError
        return np.sum(self.weights * input_data) > self.threashold

if __name__ == '__main__':
    test = Perceptron(np.array([1, 1]), 1)
    print(test.output(np.array([1, 0])))
    print(test.output(np.array([1, 1])))
