import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# # ensuring that lexicon from VADER is loaded
# nltk.download('vader_lexicon')

class SentimentOptimizer:
    def __init__(self, cleaned_texts):
        # initializes the SentimentOptimizer with a list of cleaned texts
        self.cleaned_texts = cleaned_texts
        self.sentiments = []
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment_vader(self):
        # iterates over each text in the cleaned_texts
        for text in self.cleaned_texts:
            try:
                # computes the sentiment scores using VADER. The scores include 'neg', 'neu', 'pos', and 'compound'
                scores = self.analyzer.polarity_scores(str(text))
                self.sentiments.append(scores)
            except Exception as e:
                print(f"Error processing text: {text}. Error: {e}")
                # appends a default neutral sentiment score in case of error
                self.sentiments.append({'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0})
        return self.sentiments

    def add_sentiments_to_dataframe(self, df):
        # converts the list of sentiment scores to a DataFrame
        sentiments_df = pd.DataFrame(self.sentiments)
        df = pd.concat([df.reset_index(drop=True), sentiments_df.reset_index(drop=True)], axis=1)
        # classifies sentiments based on the compound score, a score > 0.05 is positive, < -0.05 is negative, otherwise neutral
        df['sentiment'] = df['compound'].apply(
            lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
        )
        return df