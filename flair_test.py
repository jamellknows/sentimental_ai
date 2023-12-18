import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Create a SentimentIntensityAnalyzer object
    analyzer = SentimentIntensityAnalyzer()

    # Get sentiment scores
    sentiment_scores = analyzer.polarity_scores(text)

    # Determine sentiment based on the compound score
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores

if __name__ == "__main__":
    # Example usage:
    text_to_analyze = "I"

    sentiment_result, scores = analyze_sentiment(text_to_analyze)

    print(f"Sentiment: {sentiment_result}")
    print(f"Sentiment Scores: {scores}")
