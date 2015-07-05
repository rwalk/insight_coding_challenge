#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Generate testing data for the InsightDataEngineering challenge problem.

Created on Fri Jul  3 08:01:17 2015
@author: Ryan Walker
"""
import random

if __name__ == "__main__":
    vocab = []
    tweets = []
    random.seed(2)
    
    # get words and tweets out of corpus
    with open("./data/corpus.txt", "r") as f:
        for tweet in f:
            vocab.extend(tweet.split())
            tweets.append(tweet)
            
    # dedupe vocab
    vocab = list(set(vocab))

    # create test 2 -- randomly sample the tweet corpus (with replacement)
    datafile = open("./data/test2/tweets_input/tweets.txt", "w")
    ft1 = open("./data/test2/expected/ft1.txt", "w")
    ft2 = open("./data/test2/expected/ft2.txt", "w")
    words = {}
    for i in range(100):
        tweet = random.choice(tweets).strip()
        tweetl = tweet.split()
        uwc = len(set(tweetl))
        for w in tweetl:
            if words.get(w) is None:
                words[w]=1
            else:
                words[w]+=1
        datafile.write(tweet +"\n")
        ft2.write("{0}\n".format(uwc))
    for k,v in sorted(words.items(), key=lambda x: x[0]):
        ft1.write("{0:<30}{1}\n".format(k,v))
    datafile.close()
    ft1.close()
    ft2.close()
    
    # create test 3 randomly generate tweets from the vocabulary
    datafile = open("./data/test3/tweets_input/tweets.txt", "w")
    ft1 = open("./data/test3/expected/ft1.txt", "w")
    ft2 = open("./data/test3/expected/ft2.txt", "w")
    words = {}
    tweets = []
    for i in range(100):
        tweet = [random.choice(vocab) for i in range(random.randint(0,15))]
        uwc = len(set(tweet))
        for w in tweet:
            if words.get(w) is None:
                words[w]=1
            else:
                words[w]+=1
        datafile.write(" ".join(tweet) +"\n")
        ft2.write("{0}\n".format(uwc))
    for k,v in sorted(words.items(), key=lambda x: x[0]):
        ft1.write("{0:<30}{1}\n".format(k,v))
    datafile.close()
    ft1.close()
    ft2.close()