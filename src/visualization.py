import matplotlib.pyplot as plt
import numpy as np
import os


class BatteryVisualizer:

    def plot_degradation(self, capacity):

        plt.figure(figsize=(8,5))
        plt.plot(capacity)
        plt.title("Battery Capacity Degradation")
        plt.xlabel("Cycle")
        plt.ylabel("Capacity (Ah)")
        plt.grid()

        os.makedirs("outputs/plots", exist_ok=True)
        plt.savefig("outputs/plots/degradation.png")
        plt.close()


    def plot_soh(self, capacity):

        soh = capacity / capacity[0]

        plt.figure(figsize=(8,5))
        plt.plot(soh)
        plt.title("State of Health (SOH)")
        plt.xlabel("Cycle")
        plt.ylabel("SOH")
        plt.grid()

        plt.savefig("outputs/plots/soh.png")
        plt.close()


    def plot_prediction(self, y_true, y_pred):

        plt.figure(figsize=(8,5))
        plt.plot(y_true, label="Actual")
        plt.plot(y_pred, label="Predicted")
        plt.legend()
        plt.title("Capacity Prediction")
        plt.grid()

        plt.savefig("outputs/plots/prediction.png")
        plt.close()