from subReddit_Scraper import RedditScraper

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
    num_posts=250
)

# extraction of the posts and posts saved
reddit_scraper.scrape_posts()
reddit_scraper.save_posts()

# extraction of the comments and comments saved
reddit_scraper.scrape_comments()
reddit_scraper.save_comments()