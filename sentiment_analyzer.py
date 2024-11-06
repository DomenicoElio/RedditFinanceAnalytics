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

    def analyze_posts(self):
        """
        Apply the 'analyze_sentiment' method to the 'cleaned_text' column of the posts DataFrame
        This returns a tuple (sentiment_category, polarity_score) for each row
        Use zip(*) to unzip the list of tuples into two separate lists and assign them to new columns
        """
        self.cleaned_posts_df['sentiment'], self.cleaned_posts_df['polarity'] = zip(
            *self.cleaned_posts_df['cleaned_text'].apply(self.analyze_sentiment)
        )
        self.cleaned_posts_df['emotions'] = self.cleaned_posts_df['cleaned_text'].apply(self.analyze_emotions)
        return self.cleaned_posts_df

    def analyze_comments(self):
        #this function applies the same steps as the previous one, to the comments
        self.cleaned_comments_df['sentiment'], self.cleaned_comments_df['polarity'] = zip(
            *self.cleaned_comments_df['cleaned_text'].apply(self.analyze_sentiment)
        )
        self.cleaned_comments_df['emotions'] = self.cleaned_comments_df['cleaned_text'].apply(self.analyze_emotions)
        return self.cleaned_comments_df

    def save_analyzed_data(self, posts_filename='analyzed_posts.csv', comments_filename='analyzed_comments.csv'):
        # checks if the analyzed posts DataFrame is not empty before saving to the relative .csv file
        if not self.cleaned_posts_df.empty:
            self.cleaned_posts_df.to_csv(posts_filename, index=False)
        # checks if the analyzed comments DataFrame is not empty before saving to the relative .csv file
        if not self.cleaned_comments_df.empty:
            self.cleaned_comments_df.to_csv(comments_filename, index=False)
