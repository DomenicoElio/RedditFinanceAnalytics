from subReddit_Scraper import RedditScraper
from yfinance_Scraper import FinanceScraper

# configuration of the credentials necessary to query the reddit api
client_id = 'IlozIqdb7QyZ0N-BskbGOQ'
client_secret = 'Bmek46b7v4OKSzsDToati-83Jf1bnA'
user_agent = 'windows:IlozIqdb7QyZ0N-BskbGOQ:v0.1 (by u/_Domenico)'

# creating the instance of the class reddit scraper
reddit_scraper = RedditScraper(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    subreddit_name='wallstreetbets',
    num_posts=1000
)

# extraction of the posts and posts saved
reddit_scraper.scrape_posts()
reddit_scraper.save_posts()

# # extraction of the comments and comments saved
# reddit_scraper.scrape_comments()
# reddit_scraper.save_comments()

#setting the value of the tickers that I want to search for on yfinance
tickers = "TSLA"

#setting the start and end date parameters that indicate the time interval for which data needs to be pulled
start_date = '2023-10-31'
end_date = '2024-10-31'

#creating an instance of FinanceScraper
finance_scraper = FinanceScraper(
    tickers = tickers,
    start_date=start_date,
    end_date=end_date
)

#extraction and saving into a .csv file of the financial data
finance_scraper.scrape_financial_data()
finance_scraper.save_financial_data()