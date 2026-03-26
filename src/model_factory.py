import tensorflow as tf
from tensorflow import keras


class ModelFactory:
    def __init__(
        self,
        conv_filters: int = 32,
        kernel_size: int = 2,
        lstm_units: int = 50,
        dense_units: int = 1,
        learning_rate: float = 0.001
    ):
        self.conv_filters = conv_filters
        self.kernel_size = kernel_size
        self.lstm_units = lstm_units
        self.dense_units = dense_units
        self.learning_rate = learning_rate

    def create(self, input_shape: tuple) -> keras.Model:

        model = keras.Sequential([
            keras.layers.Conv1D(
                filters=self.conv_filters,
                kernel_size=self.kernel_size,
                activation="relu",
                input_shape=input_shape
            ),

            keras.layers.LSTM(self.lstm_units),

            keras.layers.Dense(self.dense_units)
        ])

        optimizer = keras.optimizers.Adam(
            learning_rate=self.learning_rate
        )

        model.compile(
            optimizer=optimizer,
            loss="mse",
            metrics=["mae"]
        )

        return model