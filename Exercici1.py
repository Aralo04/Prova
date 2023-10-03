import sys

class Neurona():
    def __init__(self, ):
        #inputs
        self.input = [3,1]
        #pesos
        self.pesos = [1,3]
        #multipliquem inputs per pesos
        i = 0
        self.total = [3, 1]
        for i in range(3):
            self.total