import praw
import pandas as pd

class RedditScraper:
    # Initializes the RedditScraper class with API credentials, subreddit name, and number of posts to scrape
    def __init__(self, client_id, client_secret,user_agent, subreddit_name, num_posts):
        # Creates a Reddit API connection using the provided client credentials
        self.reddit = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            user_agent = user_agent
        )
        # Stores the subreddit name and number of posts to scrape as instance variables
        self.subreddit_name = subreddit_name
        self.num_posts = num_posts
        # Initializes empty DataFrames to store posts and comments data
        self.posts_df = pd.DataFrame()
        self.comments_df = pd.DataFrame()

    # function that scrapes posts from the specified subreddit
    def scrape_posts(self):
        posts_data = [] # creating an empty list that will store each post's data as a dictionary

        # loops through hot posts in the specified subreddit, limited by num_posts
        for post in self.reddit.subreddit(self.subreddit_name).hot(limit=self.num_posts):
            posts_data.append({
                'post_id': post.id,
                'created_utc': post.created_utc,
                'title': post.title,
                'selftext': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
            })

        # loops through top posts in the specified subreddit, limited by num_posts
        for post in self.reddit.subreddit(self.subreddit_name).top(limit=self.num_posts):
            posts_data.append({
                'post_id': post.id,
                'created_utc': post.created_utc,
                'title': post.title,
                'selftext': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
            })

        # converts the list of dictionaries into a DataFrame
        self.posts_df = pd.DataFrame(posts_data)
        return self.posts_df

    # # function that scrapes comments for each post in the specified subreddit
    # def scrape_comments(self):
    #     comments_data = []  # creating an empty list that will store each comments data as a dictionary
    #
    #     # loops through hot posts to gather comments in the specified subreddit, limited by num_posts
    #     for post in self.reddit.subreddit(self.subreddit_name).hot(limit=self.num_posts):
    #         post.comments.replace_more(limit=0) # expands all comments loops through them
    #         for comment in post.comments.list():
    #             comments_data.append({
    #                 'post_id': post.id,
    #                 'comment_id': comment.id,
    #                 'created_utc': comment.created_utc,
    #                 'body': comment.body,
    #                 'score': comment.score
    #             })
    #
    #     # converts the list of dictionaries into a DataFrame
    #     self.comments_df = pd.DataFrame(comments_data)
    #     return self.comments_df

    #function that saves scraped posts data into a .csv file
    def save_posts(self, filename='reddit_posts.csv'):
        self.posts_df.to_csv(filename, index=False)

    # # function that saves scraped comments data into a .csv file
    # def save_comments(self, filename='reddit_comments.csv'):
    #     self.comments_df.to_csv(filename, index=False)


