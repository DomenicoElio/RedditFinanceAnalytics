import pandas as pd
import yfinance as yf

class FinanceScraper:
    """
    Class to scrape historical financial data for a list of stock tickers using yfinance.
    The initial idea, as testified by earlier pushes, was to extract a list of tickers from the data scraped from reddit,
    This first approach has been abandoned, but the infrastructure created to make it work remains the same, as it also works
    by manually passing the ticker for which data needs to be extracted
    """
    def __init__(self, tickers, start_date, end_date):
        #Initialize the FinanceScraper with a list of tickers and a date range.
        self.tickers= tickers,
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data_df = pd.DataFrame() # Create an empty DataFrame to store the scraped stock data

    def scrape_financial_data(self):
        #Scrape financial data for each ticker in the list over the specified date range.

        financial_data = [] # Initialize an empty list to hold financial data for each ticker

        # Loop through each ticker symbol in the list (the ticker is in this case only one as previously commented)
        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)   # Create a Ticker object using yfinance for the given ticker symbol
                hist = stock.history(start = self.start_date, end = self.end_date)  # Fetch historical market data for the specified date range
                if not hist.empty:
                    hist.reset_index(inplace = True)
                    hist['Ticker'] = ticker # Add a new column to indicate the ticker symbol
                    financial_data.append(hist) # Append the DataFrame to the financial_data list
            except Exception as e:
                # Print an error message if there's an issue fetching data for the ticker
                print(f'No financial data available for the following Stock Ticker: {ticker}')

        # Check if any financial data was retrieved
        if financial_data:
            self.stock_data_df = pd.concat(financial_data, ignore_index=True)
            return self.stock_data_df
        else:
            print('No financial data available')
            return pd.DataFrame()

    def save_financial_data(self, filename = 'stock_data.csv'):
        #Save the scraped financial data to a CSV file.
        if not self.stock_data_df.empty:
            self.stock_data_df.to_csv(filename, index=False)
        else:
            print('No data available to save within the DF.')

