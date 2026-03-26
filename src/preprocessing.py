from sklearn.preprocessing import MinMaxScaler

class BatteryPreprocessor:

    def transform(self, df):

        scaler = MinMaxScaler()

        X = df.drop("capacity", axis=1)

        y = df["capacity"]

        X_scaled = scaler.fit_transform(X)

        return X_scaled, y.values, scaler