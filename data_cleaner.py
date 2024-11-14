import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords

# these steps are here in order to ensure that NTLK resources are installed if not already present
# I had a few issues with punkt_tab specifically
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

class DataCleaner:
    def __init__(self, posts_df): #removed (self, posts_df, comments_df) as comments are no longer used
        # Initialize the FinanceScraper with the posts and comments df to which the relative .csv files will be assigned for analysis
        self.posts_df = posts_df
        # self.comments_df = comments_df
        # creates two new empty dataframes to fill with the data once cleaned
        self.cleaned_posts_df = pd.DataFrame()
        # self.cleaned_comments_df = pd.DataFrame()
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        # Check if text is NaN
        if pd.isnull(text):
            return ''
        # set characters to lowercase
        text = text.lower()
        # remove all URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # remove special symbols such as @ e #
        text = re.sub(r'\@\w+|\#', '', text)
        # remove numbers
        text = re.sub(r'\d+', '', text)
        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Tokenization
        tokens = nltk.word_tokenize(text)
        # Removing stop words
        filtered_words = [word for word in tokens if word not in self.stop_words]
        # Reconstructing the text
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text

    def clean_posts(self):
        # fill NaN values with empty strings
        # this error specifically caused me a lot of issues, as nan values would be evaluated as floats and cause the
        # text.lower() function to generate a type error and interrupt program execution
        self.posts_df['title'] = self.posts_df['title'].fillna('')
        self.posts_df['selftext'] = self.posts_df['selftext'].fillna('')
        # Concatenate title and selftext
        self.posts_df['cleaned_text'] = self.posts_df['title'] + ' ' + self.posts_df['selftext']
        # Apply the clean_text method
        self.posts_df['cleaned_text'] = self.posts_df['cleaned_text'].apply(self.clean_text)
        self.cleaned_posts_df = self.posts_df
        return self.cleaned_posts_df

    # def clean_comments(self):
    #     #the issue with nans doesn't really present itself in the comments
    #     self.comments_df['cleaned_text'] = self.comments_df['body'].apply(self.clean_text)
    #     self.cleaned_comments_df = self.comments_df
    #     return self.cleaned_comments_df

    def save_cleaned_data(self, posts_filename='cleaned_posts.csv'):
        #saving the cleaned posts into the relative .csv file
        if not self.cleaned_posts_df.empty:
            self.cleaned_posts_df.to_csv(posts_filename, index=False)

    # def save_cleaned_data(self, posts_filename='cleaned_posts.csv', comments_filename='cleaned_comments.csv'):
    #     #saving the cleaned posts and comments into their relative .csv files
    #     if not self.cleaned_posts_df.empty:
    #         self.cleaned_posts_df.to_csv(posts_filename, index=False)
    #     if not self.cleaned_comments_df.empty:
    #         self.cleaned_comments_df.to_csv(comments_filename, index=False)
