import pandas as pd
from matplotlib import pyplot as plt
from lda_optimizer import LDAOptimizer
from sentiment_optimizer import SentimentOptimizer

def main():
    # loading cleaned data
    cleaned_posts_df = pd.read_csv('cleaned_posts.csv')
    cleaned_texts = cleaned_posts_df['cleaned_text'].tolist()

    # optimization of the topic modeling (LDA)
    lda_optimizer = LDAOptimizer(cleaned_texts)
    lda_optimizer.preprocess_texts()
    lda_optimizer.create_dictionary_corpus()
    lda_optimizer.compute_coherence_values(start=2, limit=15, step=1)
    lda_optimizer.plot_coherence_values(start=2, limit=15, step=1)

    optimal_model, optimal_num_topics = lda_optimizer.find_optimal_number_of_topics()

    # visualization of the optimal number of topics
    topics = optimal_model.print_topics(num_words=5)
    print("\nTopic ottimali:")
    for idx, topic in topics:
        print(f'Topic {idx+1}: {topic}')

    # optimization of the sentiment analysis using VADER
    sentiment_optimizer = SentimentOptimizer(cleaned_texts)
    sentiments = sentiment_optimizer.analyze_sentiment_vader()
    analyzed_posts_df = sentiment_optimizer.add_sentiments_to_dataframe(cleaned_posts_df)

    # saving data with updated sentiments & visualization of the distribution of the sentiments
    analyzed_posts_df.to_csv('optimized_analyzed_posts.csv', index=False)
    visualize_sentiments(analyzed_posts_df)

def visualize_sentiments(analyzed_df):
    # function used to visualize the sentiment distribution
    sentiment_counts = analyzed_df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar')
    plt.title('Distribuzione dei Sentimenti (VADER)')
    plt.xlabel('Sentimento')
    plt.ylabel('Frequenza')
    plt.show()

if __name__ == '__main__':
    main()