import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


class FeatureEngineering:
    def __init__(self, data):
        self.data = data
        self.features = pd.DataFrame()
        self.target = pd.Series()

    def create_features(self):
        # creates characteristics based on financial data
        self.data['Price_Direction'] = self.data.groupby('Ticker')['Close'].shift(-1) - self.data['Close']
        # target var 1 if price rises, 0 if it remains unchanged or falls
        self.data['Target'] = self.data['Price_Direction'].apply(lambda x: 1 if x > 0 else 0)

        # # move single day sentiments to forecast future values
        self.data['compound_shifted'] = self.data.groupby('Ticker')['compound'].shift(0)
        self.data['neg_shifted'] = self.data.groupby('Ticker')['neg'].shift(0)
        self.data['neu_shifted'] = self.data.groupby('Ticker')['neu'].shift(0)
        self.data['pos_shifted'] = self.data.groupby('Ticker')['pos'].shift(0)

        # removing nans
        self.data.dropna(inplace=True)

        # defining characteristics and target
        self.features = self.data[['compound_shifted', 'neg_shifted', 'neu_shifted', 'pos_shifted', 'Volume']]
        self.target = self.data['Target']

    def scale_features(self):
        scaler = StandardScaler()
        self.features = pd.DataFrame(scaler.fit_transform(self.features), columns=self.features.columns)
        return self.features, self.target

    def get_data(self):
        return self.features, self.target