# encoding: utf-8

import numpy as np
import perceptron
import fountain

class Surface(perceptron.Perceptron):
    def __init__(self, input_num):
        self.fountains = []
        self.outputer = perceptron.Perceptron([1], 0)
        for i in range(input_num):
            self.fountains.append(fountain.Fountain())

    def output(self, input_data):
        if len(input_data) != len(self.fountains):
            print("入力数が違います")
            raise IndexError
        
        for i in range(len(input_data)):
            self.fountains[i].set(input_data[i])
        
        return self.outputer.output()

    def end(self, p):
        self.outputer.connect([p])

if __name__ == '__main__':
    data = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

    and_gate = perceptron.Perceptron(np.array([1, 1]), -1)
    nand_gate = perceptron.Perceptron(np.array([-0.7, -0.7]), 1)
    or_gate = perceptron.Perceptron(np.array([1, 1]), -0.5)
    xor_gate = Surface(2)

    xor_gate.end(and_gate)
    and_gate.connect([nand_gate, or_gate])
    nand_gate.connect(xor_gate.fountains)
    or_gate.connect(xor_gate.fountains)

    for x in data:
        print("{} : {}".format(x, xor_gate.output(x)))
