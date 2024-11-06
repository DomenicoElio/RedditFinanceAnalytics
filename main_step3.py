import pandas as pd
from lda_optimizer import LDAOptimizer

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

if __name__ == '__main__':
    main()