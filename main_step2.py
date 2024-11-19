import pandas as pd
from data_cleaner import DataCleaner
from sentiment_analyzer import SentimentAnalyzer
from topic_modeler import TopicModeler

def main():
    # loading the data extracted in step1
    posts_df = pd.read_csv('reddit_posts.csv')

    # creating an instance of data cleaner
    data_cleaner = DataCleaner(posts_df)

    # cleaning the posts & saving cleaned data into the relative .csv file
    cleaned_posts_df = data_cleaner.clean_posts()
    data_cleaner.save_cleaned_data()

    # creation of the instance of Sentiment Analyzer & analysis of sentiments and emotions on the posts
    sentiment_analyzer = SentimentAnalyzer(cleaned_posts_df)
    analyzed_posts_df = sentiment_analyzer.analyze_posts()

    # saving analyzed data
    sentiment_analyzer.save_analyzed_data()

    # topic modeling on cleaned posts
    cleaned_texts = cleaned_posts_df['cleaned_text'].tolist()
    topic_modeler = TopicModeler(cleaned_texts, num_topics=5)

    # preprocessing and creation of the dictionary and corpus
    tokenized_texts = topic_modeler.preprocess_texts()
    topic_modeler.create_dictionary_corpus(tokenized_texts)

    # definition of the lda model & visualization of the topics
    lda_model = topic_modeler.build_lda_model()
    topic_modeler.display_topics()

if __name__ == '__main__':

    main()