import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import seaborn as sns

class PredictiveModel:
    def __init__(self, features, target):
        # initializing the PredictiveModel with features and target variables
        self.features = features
        self.target = target
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.predictions = None

    def split_data(self, test_size=0.15, random_state=42):
        # splits the dataset into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features,
            self.target,
            test_size=test_size,
            random_state=random_state,
            stratify=self.target
        )

    def train_model(self):
        # training the model using XGBoost Classifier
        self.model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        # making predictions on the test set and evaluating
        self.predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, self.predictions)
        precision = precision_score(self.y_test, self.predictions)
        recall = recall_score(self.y_test, self.predictions)
        f1 = f1_score(self.y_test, self.predictions)
        print(f'Accuracy: {accuracy:.4f}')
        print(f'Precision: {precision:.4f}')
        print(f'Recall: {recall:.4f}')
        print(f'F1 Score: {f1:.4f}')
        print('\nClassification Report:')
        print(classification_report(self.y_test, self.predictions))

    def plot_confusion_matrix(self):
        # generate the confusion matrix and create heatmap
        cm = confusion_matrix(self.y_test, self.predictions)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Matrice di Confusione')
        plt.show()

    def feature_importance(self):
        # retrieve the feature importance from the trained model and visualize it
        importance = self.model.feature_importances_
        features = self.X_train.columns
        importance_df = pd.DataFrame({'Feature': features, 'Importance': importance})
        importance_df.sort_values(by='Importance', ascending=False, inplace=True)
        sns.barplot(x='Importance', y='Feature', data=importance_df)
        plt.title('Importanza delle Caratteristiche')
        plt.show()