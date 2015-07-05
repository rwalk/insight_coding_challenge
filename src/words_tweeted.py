#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Counts the occurences of words in a collection of tweets.

Assumptions:
    - Each tweet contains only ASCII characters.
    - A word is defined as anything separated by whitespace.
    - Any punctuation is part of the word itself.

Created on Fri Jul  3 08:01:17 2015
@author: Ryan Walker
"""
import argparse

class WordCounter:
    '''A very simple class to hold word counts'''
    def __init__(self):
        self.words = {}

    def insert(self,word):
        if self.words.get(word) is None:
            self.words[word] = 1
        else:
            self.words[word] += 1
    
    def items(self):
        ''' a custom iterator for word entries with keys in ascii order'''
        for k,v in sorted(self.words.items(), key=lambda x: x[0]):
            yield (k,v)

if __name__=="__main__":
    
    # cmd line argument handling
    parser = argparse.ArgumentParser(description="Count word occurences in a collection of tweets.")    
    parser.add_argument("input", help="Input file containing (preprocessed) tweets.")
    parser.add_argument("output", help="Output file.")
    args = parser.parse_args()
    
    # count tweet words
    tweet_words = WordCounter()
    with open(args.input, encoding="ASCII") as f:
        for tweet in f:
            words = tweet.split()
            for word in words:
                tweet_words.insert(word)

    # output the dictionary 
    with open(args.output, "w", encoding="ASCII") as f:
        for k,v in tweet_words.items():
            f.write("{0:<30}{1}\n".format(k,v))
