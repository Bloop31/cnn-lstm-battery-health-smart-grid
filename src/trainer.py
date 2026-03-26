from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
class Trainer:

    def run(self, model, X, y, epochs, batch):

        es = EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            shuffle=False
        )

        model.fit(
            X_train,
            y_train,
            epochs=epochs,
            batch_size=batch,
            validation_data=(X_test, y_test),
            callbacks=[es]
        )

        return model, X_test, y_test