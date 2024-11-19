import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# ensuring that lexicon from VADER is loaded
# nltk.download('vader_lexicon')

class SentimentOptimizer:
    def __init__(self, cleaned_texts):
        # initializes the SentimentOptimizer
        self.cleaned_texts = cleaned_texts
        self.sentiments = []
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment_vader(self):
        """
        iterates over each text in the cleaned_texts, computes the sentiment scores ('neg','neu','pos' and 'compound') using VADER
        and appends a default neutral sentiment score in case of error
        """
        for text in self.cleaned_texts:
            try:
                scores = self.analyzer.polarity_scores(str(text))
                self.sentiments.append(scores)
            except Exception as e:
                print(f"Error processing text: {text}. Error: {e}")
                self.sentiments.append({'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0})
        return self.sentiments

    def add_sentiments_to_dataframe(self, df):
        """
        converts the list of sentiment scores to a DataFrame and
        classifies sentiments based on the compound score: score > 0.05 is positive, < -0.05 is negative, else neutral
        """
        sentiments_df = pd.DataFrame(self.sentiments)
        df = pd.concat([df.reset_index(drop=True), sentiments_df.reset_index(drop=True)], axis=1)
        df['sentiment'] = df['compound'].apply(
            lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
        )
        return df