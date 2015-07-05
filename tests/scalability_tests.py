#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unit tests for the InsightDataEngineering challenge problem.

Created on Fri Jul  3 08:01:17 2015
@author: Ryan Walker
"""
import unittest, time
import random
from src.median_unique import Histogram
from src.words_tweeted import WordCounter

class TestScaling(unittest.TestCase):
    
    def test_word_counter_scaling(self):
        random.seed(2)
        test_words = ["yellow","movies","hamburgers","moose", "cheese", "who?","bollywood"]
        WC = WordCounter()
        for i in range(1000000):
            WC.insert(random.choice(test_words))
        print("\n")
        for k,v in WC.items():
            print("{0:<30}{1}\n".format(k,v))
        
    def test_median_scaling(self):
        H = Histogram(71)
        for i in range(100000):
            n = random.randint(0,70)
            H.insert(n)
            if i%1000==0:
                start = time.process_time()
                med = H.median()
                print("Iteration: {0}, Time: {1}, Value: {2}".format(i,time.process_time()-start,med))

if __name__ == '__main__':
    unittest.main()
