import gensim
from gensim.models import CoherenceModel
from gensim import corpora
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import nltk

class LDAOptimizer:
    def __init__(self, cleaned_texts):
        # initialize the LDAOptimizer with cleaned texts
        self.cleaned_texts = cleaned_texts
        self.tokenized_texts = []
        self.dictionary = None
        self.corpus = None
        self.models = []
        self.coherences = []

    def preprocess_texts(self):
        # tokenize each text in cleaned_texts after ensuring it's a string or bytes (nan were read as floats and caused the program to throw an error)
        self.tokenized_texts = [
            word_tokenize(str(text)) for text in self.cleaned_texts if isinstance(text, (str, bytes))
        ]

    def create_dictionary_corpus(self):
        # creates a dictionary representation of the tokenized texts
        self.dictionary = corpora.Dictionary(self.tokenized_texts)
        # converts tokenized texts to a Bag-of-Words corpus
        self.corpus = [self.dictionary.doc2bow(text) for text in self.tokenized_texts]

    def compute_coherence_values(self, start=2, limit=15, step=1):
        # iterates over the range of topic numbers
        for num_topics in range(start, limit, step):
            # build LDA model with the current number of topics
            model = gensim.models.LdaModel(
                corpus=self.corpus,
                id2word=self.dictionary,
                num_topics=num_topics,
                random_state=42,
                update_every=1,
                chunksize=100,
                passes=10,
                alpha='auto'
            )
            self.models.append(model)
            # computes coherence score using the 'c_v' metric
            coherencemodel = CoherenceModel(
                model=model,
                texts=self.tokenized_texts,
                dictionary=self.dictionary,
                coherence='c_v'
            )
            coherence = coherencemodel.get_coherence()
            self.coherences.append(coherence)
            print(f'Numero di topic: {num_topics}, Coerenza: {coherence:.4f}')

    def find_optimal_number_of_topics(self):
        # find the maximum coherence score from the list
        max_coherence = max(self.coherences)
        optimal_index = self.coherences.index(max_coherence)
        optimal_model = self.models[optimal_index]
        optimal_num_topics = optimal_model.num_topics
        print(f'Numero ottimale di topic: {optimal_num_topics}')
        return optimal_model, optimal_num_topics

    def plot_coherence_values(self, start=2, limit=15, step=1):
        # generates a range of topic numbers used
        x = range(start, limit, step)
        plt.plot(x, self.coherences)
        plt.xlabel("Numero di Topic")
        plt.ylabel("Coerenza")
        plt.title("Coerenza del Topic in funzione del Numero di Topic")
        plt.show()