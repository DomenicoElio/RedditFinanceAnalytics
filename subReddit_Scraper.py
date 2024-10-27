import praw
import pandas as pd

#The first step is dedicated to setting the credentials necessary to query the API and scrape r/wallstreetbets
#this section is created following the official praw guide available at: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html

reddit = praw.Reddit(
    client_id = 'IlozIqdb7QyZ0N-BskbGOQ',
    client_secret = 'Bmek46b7v4OKSzsDToati-83Jf1bnA',
    user_agent = 'windows:IlozIqdb7QyZ0N-BskbGOQ:v0.1 (by u/_Domenico)'
)
#as explained in the guide, a username and password are needed for authentication only when you need to analyze private comments
#this project will only take into consideration public comments, so that step is left out

#storing within a var the name of the subreddit from which posts need to be extracted
subreddit_name = 'wallstreetbets'
subreddit = reddit.subreddit(subreddit_name)

#creating a variable that indicates how many posts need to be extracted
posts_num = 500

#creating an empty list that will be used to store the scraped data
posts_data = []

#for loop that extracts the posts data
for post in subreddit.hot(limit = posts_num):
    posts_data.append({
        'post_id' : post.id,
        'created_utc' : post.created_utc,
        'title' : post.title,
        'selftext' : post.selftext,
        'score' : post.score,
        'num_comments' : post.num_comments
    })

#creating a dataframe using pandas that will contain the values of the previously created list (which contains the reddit posts)
posts_df = pd.DataFrame(posts_data)

#saving the data extracted into a .csv file for processing
posts_df.to_csv('reddit_posts.csv', index = False)

#for the sake of this project, I've also decided to extract the comments of the posts.
#this is a way to include more data as the recent api terms of service no longer allow me to pull data from a specific time frame

#creating the empty list to store scraped comments data
comments_data = []

#for loop that extracts the comments data
for post in subreddit.hot(limit = posts_num):
    post.comments.replace_more(limit = 0)
    for comment in post.comments.list():
        comments_data.append({
            'post_id': post.id,
            'comment_id': comment.id,
            'created_utc': comment.created_utc,
            'body': comment.body,
            'score': comment.score
        })

#creation of the pandas dataframe that will contain the data from the list
comments_df = pd.DataFrame(comments_data)

#saving the data onto a separate csv file for processing
comments_df.to_csv('reddit_comments.csv', index = False)