# coding: utf-8

import numpy as np
class Perceptron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.connection = []

    def output(self, input_data = None):
        if type(input_data) == type(None):
            ans = self.bias
            for i in range(len(self.weights)):
                ans += self.weights[i] * self.connection[i].output()
            return int(ans > 0)

        if len(input_data) != len(self.weights):
            print("入力数が違います")
            raise IndexError
        return int(np.sum(self.weights * input_data) + self.bias > 0)

    def connect(self, others):
        if len(others) != len(self.weights):
            print("入力数が違います")
            raise IndexError
        self.connection = others

if __name__ == '__main__':
    data = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    and_gate = Perceptron(np.array([1, 1]), -1)
    nand_gate = Perceptron(np.array([-0.7, -0.7]), 1)
    or_gate = Perceptron(np.array([1, 1]), -0.5)

    for x in data:
        print("{} : {}".format(x, and_gate.output(x)))
    print("")
    for x in data:
        print("{} : {}".format(x, nand_gate.output(x)))
    print("")
    for x in data:
        print("{} : {}".format(x, or_gate.output(x)))
