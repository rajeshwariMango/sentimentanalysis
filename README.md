# sentimentanalysis
Sentiment Analysis using python

## Code Explanation

The code consists of the following sections:

1. **Imports**: The required modules from the NLTK library are imported.
2. **word_character**: This function converts a list of words into a dictionary of features.
3. **Positive, Negative, and Neutral Word Lists**: These lists contain words associated with positive, negative, and neutral sentiments, respectively.
4. **Feature Sets**: The positive, negative, and neutral word lists are converted into feature sets using the `word_character` function.
5. **Training Set**: The feature sets are combined to create a training set.
6. **Classifier Training**: The Naive Bayes classifier is trained using the training set.
7. **Sentiment Analysis**: The code predicts the sentiment of a given sentence and calculates the ratio of positive and negative sentiments.
