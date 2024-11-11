import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import seaborn as sns

class PredictiveModel:
    def __init__(self, features, target):
        # initializes the PredictiveModel with features and target variable
        self.features = features
        self.target = target
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.predictions = None

    def split_data(self, test_size=0.2, random_state=42):
        # split the dataset into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features,
            self.target,
            test_size=test_size,
            random_state=random_state
        )

    def train_model(self):
        # instantiate the XGBoost Regressor model
        self.model = XGBRegressor(
            objective='reg:squarederror',
            random_state=42
        )
        # Train the model using the training data
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        # Use the trained model to make predictions on the test set
        self.predictions = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, self.predictions)
        r2 = r2_score(self.y_test, self.predictions)
        print(f'Mean Squared Error: {mse:.6f}')
        print(f'R^2 Score: {r2:.6f}')

    def plot_results(self):
        # create a new figure with a specified size
        plt.figure(figsize=(10, 6))
        # create a scatter plot comparing actual values vs. predictions
        sns.scatterplot(x=self.y_test, y=self.predictions)
        plt.xlabel('Valori Reali')
        plt.ylabel('Previsioni')
        plt.title('Confronto tra Valori Reali e Previsioni')
        plt.show()

    def feature_importance(self):
        # retrieves the feature importance scores from the trained model
        importance = self.model.feature_importances_
        features = self.X_train.columns
        importance_df = pd.DataFrame({'Feature': features, 'Importance': importance})
        importance_df.sort_values(by='Importance', ascending=False, inplace=True)
        sns.barplot(x='Importance', y='Feature', data=importance_df)
        plt.title('Importanza delle Caratteristiche')
        plt.show()