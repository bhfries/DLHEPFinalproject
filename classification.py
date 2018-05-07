'''
Hey guys, so this code has two inputs: "meme.txt" and "notmeme.txt" in lines 46 andd 47 respectiviely.
    Right now the code is set to read files using "ansi" encoding. This can be seen in line 25 of the code. If
    you want to use a different encoding format just make sure you change what comes after the equal sign in 
    line 25 to "utf-8", "utf-16" or whatever encoding format you're using for the text files. This program 
    outputs a text file called "output.txt" (this can be seen in line 77) that contains all the tweets that
    were correctly identified as memes, and displays them with one tweet per line. This program also prints the
    accuracy of the classifier at the end of the program (this can be seen in line 92).
    
'''
import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r', encoding="ansi")
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_tweet(tweet):
    return \
        classifier.classify(extract_features(nltk.word_tokenize(tweet)))


# read in postive and negative training tweets
pos_tweets = read_tweets('meme.txt', 'positive')
neg_tweets = read_tweets('notmeme.txt', 'negative')

# filter away words that are less than 3 letters to form the training data
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


# extract the word features out from the training data
word_features = get_word_features(\
                    get_words_in_tweets(tweets))


# get the training set and train the Naive Bayes Classifier
training_set = nltk.classify.util.apply_features(extract_features, tweets)
classifier = NaiveBayesClassifier.train(training_set)


# read in the test tweets and check accuracy
# to add your own test tweets, add them in the respective files
test_tweets = read_tweets('meme_test.txt', 'positive')
test_tweets.extend(read_tweets('notmeme_test.txt', 'negative'))
total = accuracy = float(len(test_tweets))

#creating and opening a text file called "output" to store all the positively classified tweets
file = open('output.txt','a')

#classify the tweets
for tweet in test_tweets:
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1
    if classify_tweet(tweet[0]) == tweet[1]:
        file.write(tweet[0])
        
file.close()   

#print the accuracy of the classifier
print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))
