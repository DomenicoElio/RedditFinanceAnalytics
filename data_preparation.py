import pandas as pd
import numpy as np
import re

class DataPreparation:
    def __init__(self, sentiment_data_path, financial_data_path):
        # initializes DataPreparation
        self.sentiment_data_path = sentiment_data_path
        self.financial_data_path = financial_data_path
        self.merged_data = pd.DataFrame()

    def load_data(self):
        """
        loads sentiment and emotion data, extracts tickers from text, removes entries without tickers
        and expands DataFrame if multiple tickers are mentioned. Subsequently, loads financial data
        and ensures the 'Ticker' column exists in financial data
        """
        self.sentiment_df = pd.read_csv(self.sentiment_data_path)
        self.sentiment_df['Ticker'] = self.sentiment_df['cleaned_text'].apply(self.extract_tickers)
        self.sentiment_df = self.sentiment_df[self.sentiment_df['Ticker'].notnull()]
        self.sentiment_df = self.sentiment_df.explode('Ticker')
        self.financial_df = pd.read_csv(self.financial_data_path)
        if 'Ticker' not in self.financial_df.columns:
            self.financial_df['Ticker'] = 'TSLA'
        self.financial_df['Date'] = pd.to_datetime(self.financial_df['Date'])
        self.sentiment_df['created_utc'] = pd.to_datetime(self.sentiment_df['created_utc'], unit='s')
        self.sentiment_df['Date'] = self.sentiment_df['created_utc'].dt.date

    def extract_tickers(self, text):
        if not isinstance(text, str):
            return None
        tickers = re.findall(r'\$([A-Z]{1,5})', text)
        return tickers if tickers else None

    def aggregate_sentiment(self):
        # aggregates daily sentiments for each ticker & converts the date to datetime
        aggregated_sentiment = self.sentiment_df.groupby(['Date', 'Ticker']).agg({
            'compound': 'mean',
            'neg': 'mean',
            'neu': 'mean',
            'pos': 'mean'
        }).reset_index()
        aggregated_sentiment['Date'] = pd.to_datetime(aggregated_sentiment['Date'])
        self.aggregated_sentiment = aggregated_sentiment

    def merge_data(self):
        # merges financial data with sentiment data & fills 'nan' values with the value 0
        self.merged_data = pd.merge(
            self.financial_df,
            self.aggregated_sentiment,
            on=['Date', 'Ticker'],
            how='left'
        )
        self.merged_data.fillna(0, inplace=True)
        return self.merged_data

    def save_merged_data(self, filename='merged_data.csv'):
        self.merged_data.to_csv(filename, index=False)