import re

def load(filename):
    file = open(filename)
    data = dict()
    for line in file:
        values = line.split(' ')
        data[values[0]] = float(values[1])
    file.close()
    return data