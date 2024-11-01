import pandas as pd
from data_cleaner import DataCleaner
from sentiment_analyzer import SentimentAnalyzer


def main():
    # loading the data extracted in step1 (scraped reddit data)
    posts_df = pd.read_csv('reddit_posts.csv')
    comments_df = pd.read_csv('reddit_comments.csv')

    # creating an instance of data cleaner
    data_cleaner = DataCleaner(posts_df, comments_df)

    # cleaning both posts and comments
    cleaned_posts_df = data_cleaner.clean_posts()
    cleaned_comments_df = data_cleaner.clean_comments()

    # saving cleaned data into the relative .csv files
    data_cleaner.save_cleaned_data()

    #creation of the instance of Sentiment Analyzer
    sentiment_analyzer = SentimentAnalyzer(cleaned_posts_df, cleaned_comments_df)

    # analysis of sentiments and emotions on the posts
    analyzed_posts_df = sentiment_analyzer.analyze_posts()

    # analysis of sentiments and emotions on the comments
    analyzed_comments_df = sentiment_analyzer.analyze_comments()

    # saving analyzed data
    sentiment_analyzer.save_analyzed_data()

if __name__ == '__main__':
    # executing all the steps for data cleaning
    main()