import re
import pandas as pd
import yfinance as yf
from subReddit_Scraper import posts_df

# # Combine titles and bodies of posts
# posts_df['text'] = posts_df['title'] + ' ' + posts_df['selftext']
#
# # Define the tickers for Ethereum and Bitcoin, the two stocks that this project aims to track
# desired_tickers = {'BTC', 'ETH'}
#
# # List to save the tickers found
# tickers = []
#
# for text in posts_df['text']:
#     # Find all tickers in the text
#     found_tickers = re.findall(r'\b[A-Z]{1,5}\b', text)
#     # Keep only the desired tickers (ETH and BTC)
#     found_tickers = [ticker for ticker in found_tickers if ticker in desired_tickers]
#     tickers.extend(found_tickers)
#
# # Remove duplicates
# unique_tickers = set(tickers)
# print(f'Tickers found: {unique_tickers}')

# defines the date interval for which financial data needs to be scraped
start_date = '2024-01-01'
end_date = '2024-06-30'

# list that will contain all the financial data scraped
financial_data = []

for ticker in unique_tickers:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        hist.reset_index(inplace=True)
        hist['Ticker'] = ticker
        financial_data.append(hist)
    except Exception as e:
        print(f'Errore con il ticker {ticker}: {e}')

# Concatenation  of all the dataframes
if financial_data:
    stock_data_df = pd.concat(financial_data)
    stock_data_df.to_csv('stock_data.csv', index=False)
else:
    print('Nessun dato finanziario disponibile.')