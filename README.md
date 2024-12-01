# Reddit Stock Sentiment Analysis #

This project aims to analyze the emotions and sentiments of posts from a specific subreddit on the social network Reddit.

### Obiettivo ###

The first step focuses on extracting posts and titles from a specific subreddit to analyze the expressed sentiments and emotions. 
After cleaning the data, the goal is to investigate whether there is a correlation between these sentiments and emotions (such as hype, anger, sadness, happiness) and the movement of stock prices in the stock market.

### Struttura del progetto ###

The project will consist of four parts:

### Scraping ###

The initial phase involves selecting appropriate data sources and implementing scripts for data extraction. The data comprises two main components:

   * Reddit Textual Data: Posts and comments from the selected subreddit (e.g., r/wallstreetbets) related to stock discussions.
   * Historical Stock Data: Historical data of the stocks mentioned in the subreddit posts, including prices, volume, and other financial indicators.
  
### Data Cleaning ed Analisi ###

This phase includes implementing various analytical models:

   * Sentiment Analysis: Classifies the sentiment (positive, negative, neutral) of the posts and comments.
   * Emotion Analysis: Further divides sentiment into specific emotions (e.g., anger, joy, fear) to gain more detailed insights.
   * Topic Modeling: Uses techniques like Latent Dirichlet Allocation (LDA) to identify the main topics discussed in relation to the selected stocks.

### Ottimizzazione delle Analisi ###

This phase focuses on improving the accuracy and effectiveness of the analyses:

   * LDA Optimization: Refining the topic modeling for better topic identification.
   * Sentiment Accuracy Optimization: Enhancing the precision of sentiment and emotion classification.

### Model Developement ###

In the final phase, a predictive model is developed:

   * Training and Validation: Using optimized parameters for model training and validation.
   * Final Predictions: Making forecasts on the performance of the stocks.
   * Graphical Representation: Presenting the results through visualizations

### Who do I talk to? ###

* d.bressanello@studenti.unica.it
