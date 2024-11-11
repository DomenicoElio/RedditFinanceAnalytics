import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class FeatureEngineering:
    def __init__(self, data):
        self.data = data
        self.features = pd.DataFrame()
        self.target = pd.Series()

    def create_features(self):
        # creating characteristics based on Financial data
        self.data['Return'] = self.data.groupby('Ticker')['Close'].pct_change()
        self.data['Volatility'] = self.data.groupby('Ticker')['Close'].rolling(window=7).std().reset_index(level=0, drop=True)
        # move single day sentiments to forecast future values
        self.data['compound_shifted'] = self.data.groupby('Ticker')['compound'].shift(1)
        self.data['neg_shifted'] = self.data.groupby('Ticker')['neg'].shift(1)
        self.data['neu_shifted'] = self.data.groupby('Ticker')['neu'].shift(1)
        self.data['pos_shifted'] = self.data.groupby('Ticker')['pos'].shift(1)

        # removing nans
        self.data.dropna(inplace=True)

        # defining characteristics and target
        self.features = self.data[['compound_shifted', 'neg_shifted', 'neu_shifted', 'pos_shifted', 'Volatility', 'Volume']]
        self.target = self.data['Return']

    def scale_features(self):
        scaler = StandardScaler()
        self.features = pd.DataFrame(scaler.fit_transform(self.features), columns=self.features.columns)
        return self.features, self.target

    def get_data(self):
        return self.features, self.target