import pandas as pd
from data_preparation import DataPreparation
from feature_engineering import FeatureEngineering
from predictive_model import PredictiveModel

def main():
    # preparing and processing data
    data_prep = DataPreparation(
        sentiment_data_path='optimized_analyzed_posts.csv',
        financial_data_path='stock_data.csv'
    )
    data_prep.load_data()
    data_prep.aggregate_sentiment()
    merged_data = data_prep.merge_data()
    data_prep.save_merged_data()

    # feature engineering
    feature_eng = FeatureEngineering(merged_data)
    feature_eng.create_features()
    features, target = feature_eng.scale_features()

    # development of the predictive model
    predictive_model = PredictiveModel(features, target)
    predictive_model.split_data()
    predictive_model.train_model()
    predictive_model.evaluate_model()
    predictive_model.plot_confusion_matrix()
    predictive_model.feature_importance()

if __name__ == '__main__':
    main()