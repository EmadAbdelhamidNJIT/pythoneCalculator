import math

def addition(a, b):
    return float(a) + float(b)
def subtraction(a, b):
    return float(a) - float(b)
def multiplication(a, b):
    return float(a) * float(b)
def division(a, b):
    return float(a) / float(b)
def square(a):
    return float(a) * float(a)
def squareRoot(a):
    return math.sqrt(float(a))

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        return addition(a,b)
    def subtract(self, a, b):
        return subtraction(a,b)
    def multiply(self, a, b):
        return multiplication(a,b)
    def divide(self, a, b):
        return division(a,b)
    def sqr(self, a):
        return square(a)
    def sqrRoot(self, a):
        return squareRoot(a)