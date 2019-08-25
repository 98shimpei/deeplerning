# encoding: utf-8
import perceptron
import numpy as np

class Fountain(perceptron.Perceptron):
    def __init__(self):
        self.num = 0

    def output(self):
        return self.num

    def set(self, num):
        self.num = num
