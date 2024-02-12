import nltk
from nltk.corpus import stopwords
stopwords=set(stopwords.words('english'))


pos_tweets=[('It is not impossible', 'positive'),
                    ('You are my lovely friend', 'Positive'),
                    ('She is beautiful girl', 'Positive'),
                    ('He is looking handsome', 'Positive'),
                    ('Exercise is good for health', 'Positive'),
                    ('Today\'s weather is fantastic', 'Positive'),
                    ('I love Mango', 'Positive')]

neg_tweets=[('You are my enemy friend', 'Negative'),
                    ('She is looking ugly ', 'Negative'),
                    ('He is looking horrible', 'Negative'),
                    ('Sleeping more makes you lazy', 'Negative'),
                    ('Today\'s weather is very bad', 'Negative'),
                    ('I hate Banana', 'Negative')]
#print(pos_tweets)
#print(neg_tweets)

Senti_tweets=[]
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered=[e.lower() for e in words.split() if len(e)>=3]
    Senti_tweets.append((words_filtered, sentiment))
print(Senti_tweets)

def get_words_in_tweets(tweets):
    all_words=[]
    for (words, sentiment) in Senti_tweets:
        all_words.extend(words)
    return (all_words)


def get_word_features(wordlist):
    wordlist=nltk.FreqDist(wordlist)
    word_features=wordlist.keys()
    return word_features

word_features=get_word_features(get_words_in_tweets(Senti_tweets))
print(word_features)

word_features_filtered=[]
for w in word_features:
    if w not in stopwords:
        word_features_filtered.append(w)

print(word_features_filtered)

def extract_features(document):
    document_words=set(document)
    features={}
    for word in word_features_filtered:
        features['contains(%s)' %word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, Senti_tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

test_tweet='This is a horrible book'
print("{}: Sentiment={}".format(test_tweet, classifier.classify(extract_features(test_tweet.split()))))