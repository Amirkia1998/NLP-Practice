import nltk
from nltk.corpus import movie_reviews

# TASK 1 =========================================================
# # Check the corpus name and size
# print(f"Corpus Name: {movie_reviews.__name__}")
# print(f"Corpus Size: {len(movie_reviews.fileids())} files")
#
# # Count the number of positive and negative reviews
# pos_reviews = movie_reviews.fileids('pos')
# neg_reviews = movie_reviews.fileids('neg')
# print(f"Positive Reviews: {len(pos_reviews)} files")
# print(f"Negative Reviews: {len(neg_reviews)} files")
# TASK 2 =========================================================
# # Define the short review
# review = "Mr. Matt Damon was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."
#
# # Lowercase the text
# review = review.lower()
#
# # Tokenize the text
# tokens = nltk.word_tokenize(review)
#
# # Define a function to generate a feature dictionary for a given document
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features
#
# # Generate the word feature dictionary
# all_words = nltk.FreqDist(movie_reviews.words())
# word_features = list(all_words.keys())[:2000]
# featureset = document_features(tokens)
#
# # Load the Naive Bayes Classifier and classify the review
# classifier = nltk.NaiveBayesClassifier.train([(featureset, '')])
# classification = classifier.classify(featureset)
#
# # Calculate the classification probabilities
# prob_dist = classifier.prob_classify(featureset)
# pos_prob = prob_dist.prob('pos')
# neg_prob = prob_dist.prob('neg')
#
# # Print the results
# print("Classification: {}".format(classification))
# print("Positive Probability: {:.2%}".format(pos_prob))
# print("Negative Probability: {:.2%}".format(neg_prob))
# TASK 3 =========================================================
# # Define the short review
# review = "Mr. Steven Seagal was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."
#
# # Lowercase the text
# review = review.lower()
#
# # Tokenize the text
# tokens = nltk.word_tokenize(review)
#
# # Define a function to generate a feature dictionary for a given document
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features
#
# # Generate the word feature dictionary
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words.keys())[:2000]
# featureset = document_features(tokens)
#
# # Load the Naive Bayes Classifier and classify the review
# classifier = nltk.NaiveBayesClassifier.train([(featureset, '')])
# classification = classifier.classify(featureset)
#
# # Calculate the classification probabilities
# prob_dist = classifier.prob_classify(featureset)
# pos_prob = prob_dist.prob('pos')
# neg_prob = prob_dist.prob('neg')
#
# # Print the results
# print("Classification: {}".format(classification))
# print("Positive Probability: {:.2%}".format(pos_prob))
# print("Negative Probability: {:.2%}".format(neg_prob))
# TASK 4 =========================================================
import nltk
from nltk.corpus import movie_reviews

# Define the short review
review = "Mr. Matt Damon was outstanding, fantastic."

# Lowercase the text
review = review.lower()

# Tokenize the text
tokens = nltk.word_tokenize(review)

# Define a function to generate a feature dictionary for a given document
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# Generate the word feature dictionary
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:2000]
featureset = document_features(tokens)

# Load the Naive Bayes Classifier and classify the review
classifier = nltk.NaiveBayesClassifier.train([(featureset, '')])
classification = classifier.classify(featureset)

# Calculate the classification probabilities
prob_dist = classifier.prob_classify(featureset)
pos_prob = prob_dist.prob('pos')
neg_prob = prob_dist.prob('neg')

# Print the results
print("Classification: {}".format(classification))
print("Positive Probability: {:.2%}".format(pos_prob))
print("Negative Probability: {:.2%}".format(neg_prob))
# TASK 5 =========================================================
classifier = nltk.NaiveBayesClassifier.train([(featureset, '')])
classifier.show_most_informative_features(30)
