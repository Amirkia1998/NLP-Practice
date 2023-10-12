
# =========================================================================================
import nltk
from nltk.corpus import gutenberg
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.lm import MLE
from nltk.tokenize.treebank import TreebankWordDetokenizer

moby_dick = gutenberg.raw('melville-moby_dick.txt')
# print(moby_dick)

# total number of words
print("Number of words =", len(gutenberg.words("melville-moby_dick.txt")))
# total number of chars
print("Number of chars =", len(moby_dick))
# number of words ?
print("Number of words =", len(list(nltk.word_tokenize(moby_dick))))
# vocab size (number of unique words)
print("Vocab Size =", len(set(nltk.word_tokenize(moby_dick))))
print()

# first tokenize sentences and then words
tokenized_text = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(moby_dick)]
# print(tokenized_text)

# create padded 1, 2, ... n grams pipeline
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)

# Create a Train model
model = MLE(n)
model.fit(train_data, padded_sents)

# Evaluation
print("Vocab Length: ", len(model.vocab))
print()
print("count(breath | my last) =", model.counts[["my", "last"]]["breath"])
print("count(am | I) =", model.counts[["am"]]["i"])
print()
print("P(the | I am) =", model.score("the", ["i", "am"]))
print("P(pizza | I am) =", model.score("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.score("stars", ["home", "among", "the"]))
print()
print("P(the | I am) =", model.logscore("the", ["i", "am"]))
print("P(pizza | I am) =", model.logscore("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.logscore("stars", ["home", "among", "the"]))
print()
print("Perplexity of (involved in | the matter)", model.perplexity([("involved", "in"), ("the", "matter")]))
print("Perplexity of (have the fear | of death)", model.perplexity([("have", "the", "fear"), ("of", "death")]))
print()

# Generate Sentences
detokenize = TreebankWordDetokenizer().detokenize
print(detokenize(model.generate(10, text_seed=['pizza'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['book'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['whale'], random_seed=10)))


# ===============================================================================================
import nltk
from nltk.corpus import inaugural
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.lm import MLE
from nltk.tokenize.treebank import TreebankWordDetokenizer

obama = inaugural.raw('2009-Obama.txt')
# print(obama)

# total number of words
print("Number of words =", len(inaugural.words("2009-Obama.txt")))
# total number of chars
print("Number of chars =", len(obama))
# number of words ?
print("Number of words =", len(list(nltk.word_tokenize(obama))))
# vocab size (number of unique words)
print("Vocab Size =", len(set(nltk.word_tokenize(obama))))
print()

# first tokenize sentences and then words
tokenized_text = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(obama)]
# print(tokenized_text)

# create padded 1, 2, ... n grams pipeline
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)

# Create a Train model
model = MLE(n)
model.fit(train_data, padded_sents)

# Evaluation
print("Vocab Length: ", len(model.vocab))
print()
print("count(breath | my last) =", model.counts[["my", "last"]]["breath"])
print("count(am | I) =", model.counts[["am"]]["i"])
print()
print("P(the | I am) =", model.score("the", ["i", "am"]))
print("P(pizza | I am) =", model.score("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.score("stars", ["home", "among", "the"]))
print()
print("P(the | I am) =", model.logscore("the", ["i", "am"]))
print("P(pizza | I am) =", model.logscore("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.logscore("stars", ["home", "among", "the"]))
print()
print("Perplexity of (involved in | the matter)", model.perplexity([("involved", "in"), ("the", "matter")]))
print("Perplexity of (have the fear | of death)", model.perplexity([("have", "the", "fear"), ("of", "death")]))
print()

# Generate Sentences
detokenize = TreebankWordDetokenizer().detokenize
print(detokenize(model.generate(10, text_seed=['pizza'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['book'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['whale'], random_seed=10)))


# ======================================================================================

import nltk
from nltk.corpus import nps_chat
from nltk.corpus import gutenberg
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.lm import MLE
from nltk.tokenize.treebank import TreebankWordDetokenizer

# because nps_chat has many txt files associated with it syntax is different
chat = nps_chat.raw()
# the format of this text is different from the prev texts
print(chat)

# total number of words
print("Number of words =", len(nps_chat.words()))
# total number of chars
print("Number of chars =", len(chat))
# number of words ?
print("Number of words =", len(list(nltk.word_tokenize(chat))))
# vocab size (number of unique words)
print("Vocab Size =", len(set(nltk.word_tokenize(chat))))
print()

# first tokenize sentences and then words
tokenized_text = [list(map(str.lower, word_tokenize(sent))) for sent in sent_tokenize(chat)]
# print(tokenized_text)

# create padded 1, 2, ... n grams pipeline
n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)

# Create a Train model
model = MLE(n)
model.fit(train_data, padded_sents)

# Evaluation
print("Vocab Length: ", len(model.vocab))
print()
print("count(breath | my last) =", model.counts[["my", "last"]]["breath"])
print("count(am | I) =", model.counts[["am"]]["i"])
print()
print("P(the | I am) =", model.score("the", ["i", "am"]))
print("P(pizza | I am) =", model.score("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.score("stars", ["home", "among", "the"]))
print()
print("P(the | I am) =", model.logscore("the", ["i", "am"]))
print("P(pizza | I am) =", model.logscore("pizza", ["i", "am"]))
print("P(stars | home among the) =", model.logscore("stars", ["home", "among", "the"]))
print()
print("Perplexity of (involved in | the matter)", model.perplexity([("involved", "in"), ("the", "matter")]))
print("Perplexity of (have the fear | of death)", model.perplexity([("have", "the", "fear"), ("of", "death")]))
print()

# Generate Sentences
detokenize = TreebankWordDetokenizer().detokenize
print(detokenize(model.generate(10, text_seed=['pizza'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['book'], random_seed=10)))
print(detokenize(model.generate(10, text_seed=['whale'], random_seed=10)))
