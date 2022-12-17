import sys as system
import math
import numpy as np
import chars

# 25 входных нейронов - буквы
# 2 выходных нейрона - (1): употреблен мат

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train():
    pass

def get_result():
    pass

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
 
    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения 
        # и последующее использование функции активации
 
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

def main(args):
    a = chars.ru_load('data/ru_chars.txt')
    for i in a:
        print(i)


if __name__ == '__main__':
    main(system.argv)