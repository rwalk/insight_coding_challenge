#!/bin/bash

python3 src/words_tweeted.py tweets_input/tweets.txt tweets_output/f1.txt
python3 src/median_unique.py tweets_input/tweets.txt tweets_output/f2.txt
