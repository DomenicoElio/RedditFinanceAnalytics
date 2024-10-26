import praw
import pandas as pd

#The first step is dedicated to setting the credentials necessary to query the API and scrape r/wallstreetbets
#this section is created following the official praw guide available at: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html

reddit = praw.Reddit(
    client_id = 'Finance_Scraper',
    client_secret = 'Bmek46b7v4OKSzsDToati-83Jf1bnA',
    user_agent = 'windows:IlozIqdb7QyZ0N-BskbGOQ:v0.1 (by u/_Domenico)'
)
#as explained in the guide, a username and password are needed for authentication only when you need to analyze private comments
#this project will only take into consideration public comments, so that step is left out