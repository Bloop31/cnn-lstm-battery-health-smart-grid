import numpy as np


class HealthCalculator:

    def compute_soh(self, capacity):

        return capacity / capacity[0]

    def compute_rul(self, capacity, threshold=0.7):

        soh = self.compute_soh(capacity)

        idx = np.where(soh < threshold)[0]

        if len(idx) == 0:
            return len(capacity)

        return idx[0]