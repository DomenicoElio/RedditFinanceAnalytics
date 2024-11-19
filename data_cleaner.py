import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords

# installing the necessary resources and packages to execute the code
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

class DataCleaner:
    def __init__(self, posts_df):
        """
        initializes the DataCleaner creating the DataFrame that will store cleaned posts and
        creates two new empty dataframes to fill with the data once cleaned
        """
        self.posts_df = posts_df
        self.cleaned_posts_df = pd.DataFrame()
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """
        method handles 'nan' values, set characters to lowercase, removes all URLs, remove special symbols such as @ e #
        remove numbers and punctuation, carries out tokenization, removes stop words and reconstructs the text
        """
        if pd.isnull(text):
            return ''
        text = text.lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\@\w+|\#', '', text)
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        filtered_words = [word for word in tokens if word not in self.stop_words]
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text

    def clean_posts(self):
        """
        fill NaN values with empty strings: these would be evaluated as floats and cause the
        text.lower() function to generate a type error and interrupt program execution
        """
        self.posts_df['title'] = self.posts_df['title'].fillna('')
        self.posts_df['selftext'] = self.posts_df['selftext'].fillna('')
        self.posts_df['cleaned_text'] = self.posts_df['title'] + ' ' + self.posts_df['selftext']
        self.posts_df['cleaned_text'] = self.posts_df['cleaned_text'].apply(self.clean_text)
        self.cleaned_posts_df = self.posts_df
        return self.cleaned_posts_df

    def save_cleaned_data(self, posts_filename='cleaned_posts.csv'):
        #saving the cleaned posts into the relative .csv file
        if not self.cleaned_posts_df.empty:
            self.cleaned_posts_df.to_csv(posts_filename, index=False)