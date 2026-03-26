from sklearn.metrics import mean_squared_error
import numpy as np


class Evaluator:

    def check(self, model, X_test, y_test):

        pred = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, pred))

        print("Final RMSE =", rmse)