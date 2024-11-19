import pandas as pd
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# downloads the 'punkt' tokenizer for NLTK
#nltk.download('punkt')

class TopicModeler:
    def __init__(self, cleaned_texts, num_topics = 5):
        """
        initialize the TopicModeler with cleaned texts and the number of topics to extract and
        initializes placeholders for the dictionary, corpus, and LDA model
        """
        self.cleaned_texts = cleaned_texts
        self.num_topics = num_topics
        self.dictionary = None
        self.corpus = None
        self.lda_model = None

    def preprocess_texts(self):
        # tokenizes each text in 'cleaned_texts'
        tokenized_texts = [word_tokenize(text) for text in self.cleaned_texts]
        return tokenized_texts

    def create_dictionary_corpus(self, tokenized_texts):
        # creates a dictionary mapping of words to unique IDs and convert tokenized texts into a bag-of-words corpus based on the dictionary
        self.dictionary = corpora.Dictionary(tokenized_texts)
        self.corpus = [self.dictionary.doc2bow(text) for text in tokenized_texts]

    def build_lda_model(self):
        # builds the LDA (Latent Dirichlet Allocation) model using Gensim
        self.lda_model = gensim.models.ldamodel.LdaModel(
            corpus = self.corpus,
            id2word=self.dictionary,
            num_topics=self.num_topics,
            random_state=42,
            update_every=1,
            chunksize=100,
            passes=10,
            alpha='auto',
            per_word_topics=True
        )
        return self.lda_model

    def display_topics(self):
        """
        checks if the dictionary is available, gets the topic terms, converts word IDs to words
        and generates & displays a WordCloud from the word frequencies
        """
        if self.dictionary is None:
            print("Dictionary is not available.")
            return

        for idx in range(self.num_topics):
            topic = self.lda_model.get_topic_terms(topicid=idx, topn=5)
            print(f'\nTopic {idx}:')
            print('Raw topic data:', topic)

            topic_dict = {}
            for word_id, weight in topic:
                word = self.dictionary[word_id]
                topic_dict[word] = weight
            print('Topic dictionary:', topic_dict)

            if topic_dict:
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color='white'
                ).generate_from_frequencies(topic_dict)

                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'Topic {idx} Word Cloud')
                plt.show()
            else:
                print("No valid terms found for this topic.")

    def get_document_topics(self):
        # initializes a list to hold the topic distribution for each document
        doc_topics = []
        for doc in self.corpus:
            doc_topics.append(self.lda_model.get_document_topics(doc))
        return doc_topics