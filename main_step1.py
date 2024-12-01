from subReddit_Scraper import RedditScraper
from yfinance_Scraper import FinanceScraper

def main():
    # configuration of the credentials necessary to query the reddit api
    # make sure to insert the correct app client id and secret - these only referred to the app created for this project and are no longer active
    client_id = 'IlozIqdb7QyZ0N-BskbGOQ'
    client_secret = 'Bmek46b7v4OKSzsDToati-83Jf1bnA'
    user_agent = 'windows:IlozIqdb7QyZ0N-BskbGOQ:v0.1 (by u/username)'

    # creating the instance of the class reddit scraper
    reddit_scraper = RedditScraper(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        subreddit_name='wallstreetbets',
        num_posts=1000
    )

    # extraction and saving of the reddit posts
    reddit_scraper.scrape_posts()
    reddit_scraper.save_posts()

    # setting the value of the tickers that I want to search for on yfinance
    tickers = "TSLA"

    # setting the start and end date parameters that indicates the time interval for which data needs to be pulled
    start_date = '2024-03-31'
    end_date = '2024-10-31'

    # creating an instance of FinanceScraper
    finance_scraper = FinanceScraper(
        tickers = tickers,
        start_date=start_date,
        end_date=end_date
    )

    # extracting financial data and saving it into a .csv file
    finance_scraper.scrape_financial_data()
    finance_scraper.save_financial_data()

if __name__ == '__main__':

    main()
