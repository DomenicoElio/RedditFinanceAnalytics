import pandas as pd
from textblob import TextBlob
from nrclex import NRCLex
from textblob.en import sentiment


class SentimentAnalyzer:
    def __init__(self, cleaned_posts_df, cleaned_comments_df):
    # Initialize the sentiment analyzer with the posts and comments df obtained in data cleaning
        self.cleaned_posts_df = cleaned_posts_df
        self.cleaned_comments_df = cleaned_comments_df

    def analyze_sentiment(self, text):
        # create a TextBlob object from the input text
        blob = TextBlob(text)
        # extract the sentiment polarity from the TextBlob object
        sentiment_polarity = blob.sentiment.polarity
        # Determine the sentiment category based on the polarity score
        if sentiment_polarity > 0:
            sentiment = 'positive'
        elif sentiment_polarity == 0:
            sentiment = 'neutral'
        else:
            sentiment = 'negative'
        return sentiment, sentiment_polarity

    def analyze_emotions(self, text):
        # create an NRCLex object to analyze emotions in the text
        emotion = NRCLex(text)
        # get the top emotions detected in the text as a list of tuples (emotion, score)
        emotions = emotion.top_emotions
        return emotions


