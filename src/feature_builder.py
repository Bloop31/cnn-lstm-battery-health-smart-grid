import numpy as np

class SequenceBuilder:

    def __init__(self, window):
        self.window = window

    def build(self, X, y):

        Xs = []
        ys = []

        for i in range(len(X) - self.window):

            Xs.append(X[i:i+self.window])
            ys.append(y[i+self.window])

        return np.array(Xs), np.array(ys)