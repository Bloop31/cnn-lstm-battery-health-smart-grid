import pandas as pd
import os
import numpy as np


class CSVBatteryLoader:

    def __init__(self, folder_path, max_files):
        self.folder_path = folder_path
        self.max_files = max_files

    def get_array(self, df, possible):

        for col in possible:
            if col in df.columns:
                return df[col].values

        return None

    def safe_mean(self, arr):

        if arr is None:
            return np.nan

        return np.nanmean(arr)

    def compute_capacity(self, df):

        current = self.get_array(
            df,
            ["Current_measured", "Current_load", "Current"]
        )

        time = self.get_array(
            df,
            ["Time", "Test_Time", "Step_Time"]
        )

        if current is None or time is None:
            return np.nan

        dt = np.diff(time, prepend=time[0])

        cap = np.sum(np.abs(current) * dt) / 3600

        return cap

    def load(self):

        files = sorted(os.listdir(self.folder_path))

        dataset = []
        count = 0

        for f in files:

            if f.endswith(".csv"):

                path = os.path.join(self.folder_path, f)

                df = pd.read_csv(path)

                voltage = self.get_array(
                    df,
                    ["Voltage_measured", "Voltage_load", "Voltage_charge", "Voltage"]
                )

                current = self.get_array(
                    df,
                    ["Current_measured", "Current_load", "Current_charge", "Current"]
                )

                temp = self.get_array(
                    df,
                    ["Temperature_measured", "Temperature"]
                )

                cap = self.compute_capacity(df)

                row = {
                    "cycle": count,
                    "voltage_mean": self.safe_mean(voltage),
                    "current_mean": self.safe_mean(current),
                    "temp_mean": self.safe_mean(temp),
                    "capacity": cap
                }

                dataset.append(row)

                count += 1

                if count >= self.max_files:
                    break

        df_final = pd.DataFrame(dataset)

        df_final = df_final.dropna()

        return df_final