# coding: utf-8
import numpy as np
import perceptron

class And(perceptron.Perceptron):
    def __init__(self):
        super().__init__([0.5, 0.5], -0.7)


if __name__  == '__main__':
    a = And()
    print(a.output(np.array([1, 1])))
    print(a.output(np.array([0, 1])))

