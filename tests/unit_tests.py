#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unit tests for the InsightDataEngineering challenge problem.

Created on Fri Jul  3 08:01:17 2015
@author: Ryan Walker
"""
import unittest
import random
from statistics import median
from src.median_unique import Histogram
from src.words_tweeted import WordCounter

class TestTweetMethods(unittest.TestCase):
    
    def test_median(self):
        random.seed(2)
        range_limit = 70
        n_reps = 500
        n_values = 1000
        for i in range(n_reps):
            H = Histogram(range_limit+1)
            values = [random.randint(0,range_limit) for j in range(n_values)]
            for v in values:
                H.insert(v)
            self.assertEqual(H.median(), median(values), "Median incorrect!")
            
    def test_word_counter(self):
        WC = WordCounter()        
        test_words = ["purple","purple","cat","monkey","dog","Monkey","doNkey"]
        for w in test_words:
            WC.insert(w)
        self.assertEqual(WC.words["purple"], 2, "Word count incorrect.")
        self.assertEqual(WC.words["monkey"], 1, "Word count incorrect.")

if __name__ == '__main__':
    unittest.main()
