import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def word_character(words):
    return dict([(word, True) for word in words])
 
positive_word = [ 'awesome', 'interesting','fabulous','lovely','outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
negative_word = ['dislike', 'horrible','gross','bad','worse', 'terrible','useless', 'hate', 'meaningless','waste',':(' ]
neutral_word = [ 'movie','think','game','program','project','the','sound','was','is','actors','did','know','words','not' ]
 
positive_character = [(word_character(pos), 'pos') for pos in positive_word]
negative_character = [(word_character(neg), 'neg') for neg in negative_word]
neutral_character = [(word_character(neu), 'neu') for neu in neutral_word]
 
train_set = negative_character + positive_character + neutral_character
 
classifier = NaiveBayesClassifier.train(train_set) 
# Prediction

neg = 0
pos = 0
sentence = "awesome moive, I like it"
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify( word_character(word))
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'pos':
        pos = pos + 1
 
print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))
