import pandas as pd
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
import nltk

# Download the 'punkt' tokenizer for NLTK
nltk.download('punkt')

class TopicModeler:
    def __init__(self, cleaned_texts, num_topics = 5):
        # initialize the TopicModeler with cleaned texts and the number of topics to extract
        self.cleaned_texts = cleaned_texts
        self.num_topics = num_topics
        # initialize placeholders for the dictionary, corpus, and LDA model
        self.dictionary = None
        self.corpus = None
        self.lda_model = None

    def preprocess_texts(self):
        # tokenize each text in 'cleaned_texts'
        tokenized_texts = [word_tokenize(text) for text in self.cleaned_texts]
        return tokenized_texts

    def create_dictionary_corpus(self, tokenized_texts):
        # create a dictionary mapping of words to unique IDs and convert tokenized texts into a bag-of-words corpus based on the dictionary
        self.dictionary = corpora.Dictionary(tokenized_texts)
        self.corpus = [self.dictionary.doc2bow(text) for text in tokenized_texts]

    def build_lda_model(self):
        # build the LDA (Latent Dirichlet Allocation) model using Gensim
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
        # retrieve the topics along with their top words (this will potentially dictate the selection of the tickers for the yfinance scrape)
        topics = self.lda_model.print_topics(num_words=5)
        for idx, topic in topics:
            print(f'Topics {idx+1}: {topic}')

    def get_document_topics(self):
        # initialize a list to hold the topic distribution for each document
        doc_topics = []
        for doc in self.corpus:
            doc_topics.append(self.lda_model.get_document_topics(doc))
        return doc_topics

