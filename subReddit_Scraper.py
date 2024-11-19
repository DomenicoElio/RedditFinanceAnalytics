import praw
import pandas as pd

class RedditScraper:
    # Initializes the RedditScraper class with API credentials, subreddit name, and number of posts to scrape
    def __init__(self, client_id, client_secret,user_agent, subreddit_name, num_posts):
        """
        creates a Reddit API connection using the provided client credentials
        stores the subreddit name and number of posts to scrape as instance variables
        initializes empty DataFrames to store posts and comments data
        """
        self.reddit = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            user_agent = user_agent
        )
        self.subreddit_name = subreddit_name
        self.num_posts = num_posts
        self.posts_df = pd.DataFrame()
        self.comments_df = pd.DataFrame()

    def scrape_posts(self):
        """
        scrapes posts from the specified subreddit, storing the content as a list of dictionaries
        subsequently saving the data in a DataFrame
        """
        posts_data = []

        for post in self.reddit.subreddit(self.subreddit_name).hot(limit=self.num_posts):
            posts_data.append({
                'post_id': post.id,
                'created_utc': post.created_utc,
                'title': post.title,
                'selftext': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
            })

        for post in self.reddit.subreddit(self.subreddit_name).top(limit=self.num_posts):
            posts_data.append({
                'post_id': post.id,
                'created_utc': post.created_utc,
                'title': post.title,
                'selftext': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
            })
        self.posts_df = pd.DataFrame(posts_data)
        return self.posts_df

    #function that saves scraped posts data into a .csv file
    def save_posts(self, filename='reddit_posts.csv'):
        self.posts_df.to_csv(filename, index=False)