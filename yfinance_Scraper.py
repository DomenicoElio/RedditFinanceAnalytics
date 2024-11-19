import pandas as pd
import yfinance as yf

class FinanceScraper:
    """
    class to scrape historical financial data for a list of stock tickers using yfinance.
    a single ticker is passed manually on execution
    """
    def __init__(self, tickers, start_date, end_date):
        """
        initializes the FinanceScraper with a list of tickers and a date range
        additionally, create an empty DataFrame to store the scraped stock data
        """
        self.tickers= tickers,
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data_df = pd.DataFrame()

    def scrape_financial_data(self):
        """
        scrapes financial data for each ticker over the specified date range.
        The code is intended to also accept a list of tickers and extract data for each one
        """
        financial_data = []

        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(start = self.start_date, end = self.end_date)
                if not hist.empty:
                    hist.reset_index(inplace = True)
                    hist['Ticker'] = ticker
                    financial_data.append(hist)
            except Exception as e:
                print(f'No financial data available for the following Stock Ticker: {ticker}')

        # checks if any financial data was retrieved
        if financial_data:
            self.stock_data_df = pd.concat(financial_data, ignore_index=True)
            return self.stock_data_df
        else:
            print('No financial data available')
            return pd.DataFrame()

    def save_financial_data(self, filename = 'stock_data.csv'):
        # saves the scraped financial data to a CSV file.
        if not self.stock_data_df.empty:
            self.stock_data_df.to_csv(filename, index=False)
        else:
            print('No data available to save within the DF.')

