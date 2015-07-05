#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Compute the running median unique word count/per tweet for a collection of tweets.

Assumptions:
    - Each tweet contains only ASCII characters.
    - A word is defined as anything separated by whitespace.
    - Any punctuation is part of the word itself.

A tweet has at most 140 characters.  That leaves upto 70 unique words per tweet.
Thus unique word count per tweet takes on a discrete set of values in the range
0-70.  A histogram counts the number of occurences 


Created on Fri Jul  3 08:01:17 2015
@author: Ryan Walker
"""
import argparse

class Histogram:
    ''' This class maintains a histogram for a given value range and
        allows for constant time computation of order statistics.
    '''
    def __init__(self, N):
        self.data = [0]*N
        self.size = 0
        self.N = N

    def insert(self,value):
        assert(0<=value and value<self.N)
        self.data[value]+=1    
        self.size+=1
            
    def order_statistic(self, n):
        '''find the n-th order value in the histogram.'''
        value, n_observed = 0,0
        # Walk the array until we pass the n-th order value
        for i in range(len(self.data)):
            n_observed+=self.data[i]
            if n_observed>n:
                break
            value+=1
        return(value)
     
    def median(self):
        '''Compute median from the histogram array A'''    
        midpoint = self.size//2        
        if self.size%2==1:
            return(self.order_statistic(midpoint))
        else:
            return((self.order_statistic(midpoint)+self.order_statistic(midpoint-1))/2.0)

    def __str__(self):
        val = ""
        for k,v in enumerate(self.data):
            val+="{0:<5}{1}\n".format(k,v)
        return(val)

if __name__=="__main__":
    
    # cmd line argument handling
    parser = argparse.ArgumentParser(description="Compute running median of unique word count per tweet for a collection of tweets.")    
    parser.add_argument("input", help="Input file containing (preprocessed) tweets.")
    parser.add_argument("output", help="Output file.")
    args = parser.parse_args()

    # histogram for word counts with values ranging from 0 to 70 inclusive
    unique_word_count_histogram = Histogram(71)
    
    # For each tweet, update the histogram and print its median.
    with open(args.input, encoding="ASCII") as infile:
        with open(args.output, "w", encoding="ASCII") as outfile:
            for tweet in infile:
                
                # count unique words in the tweet
                uwc = len(set(tweet.split()))

                # update histogram
                unique_word_count_histogram.insert(uwc)

                # compute the new median
                outfile.write("{0}\n".format(unique_word_count_histogram.median()))
