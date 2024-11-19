import pandas as pd
from textblob import TextBlob
from nrclex import NRCLex
from textblob.en import sentiment

class SentimentAnalyzer:
    def __init__(self, cleaned_posts_df):
    # Initialize SentimentAnalyzer passing the posts_df obtained in data cleaning
        self.cleaned_posts_df = cleaned_posts_df

    def analyze_sentiment(self, text):
        """
        creates a TextBlob object from the input text, extracts the sentiment polarity from the TextBlob object
        and determines the sentiment category based on the polarity score
        """
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        if sentiment_polarity > 0:
            sentiment = 'positive'
        elif sentiment_polarity == 0:
            sentiment = 'neutral'
        else:
            sentiment = 'negative'
        return sentiment, sentiment_polarity

    def analyze_emotions(self, text):
        """
        creates an NRCLex object to analyze emotions in the text & gets
        top emotions detected in the text as a list of tuples (emotion, score)
        """
        emotion = NRCLex(text)
        emotions = emotion.top_emotions
        return emotions

    def analyze_posts(self):
        """
        applies the 'analyze_sentiment' method to the 'cleaned_text' column of the posts DataFrame
        this returns a tuple (sentiment_category, polarity_score) for each row
        Uses zip(*) to unzip the list of tuples into two separate lists and assign them to new columns
        """
        self.cleaned_posts_df['sentiment'], self.cleaned_posts_df['polarity'] = zip(
            *self.cleaned_posts_df['cleaned_text'].apply(self.analyze_sentiment)
        )
        self.cleaned_posts_df['emotions'] = self.cleaned_posts_df['cleaned_text'].apply(self.analyze_emotions)
        return self.cleaned_posts_df

    def save_analyzed_data(self, posts_filename='analyzed_posts.csv'):
        # checks if the analyzed posts DataFrame is not empty before saving to the relative .csv file
        if not self.cleaned_posts_df.empty:
            self.cleaned_posts_df.to_csv(posts_filename, index=False)