Insight Data Engineering - Coding Challenge [Solution]
===========================================================

## Description

This is a Python3 solution to the [Insight Data Science Coding Challenge Problem](https://github.com/InsightDataScience/cc-example).

To run the solution on a Linux/UNIX system, simply execute the `run.sh script` in the top-level directory.

The folder `tests/` contains a series of unit tests, scalability tests, and end-to-end tests, all of which can be run from `tests/` by executing `runtests.sh`.

## Solution description

### Word frequency distributions
The first part of the challenge asks us to maintain a word frequency distribution for tweets.  Each time a new tweet is received, we should update the frequency distribution.  We should be able to report the current frequency for a given word in real time.

Using a key-value dictionary, it is straightforward to implement an `O[1]` time complexity solution.
When a new tweet arrives, we take each word and check if it is present in the dictionary.  If the word is not found,
we add the word as a new key in the dictionary and set the value for that key to 1.  If the word is already a key in the dictionary, we just increment the value for the word's key by 1. Since dictionaries provide amortized constant-time lookup and insert, this solution is average `O[1]` in time.  In other words, processing the 10 billionth tweet should take about the same time as processing the first tweet. 

In terms of space complexity, the dictionary size will be proportional to the size of the vocabulary used in all the tweets received so far.  Since we can query specific values in the dictionary in constant time, we can report the frequency of a given word in constant time.  Enumerating the entire frequency distribution for all words will have a complexity that is linear in the size of the dictionary.

### Median unique words per tweet
The second part of the challenge asks us to track the median unique word count per tweet.  Each time a new tweet is received, the median needs to be recomputed and the new median value needs to be reported back in real time.

In general, computation of a running median is very difficult to scale; one approach is to maintain the data in a sorted order list and track the middle element. Since insert into the sorted list will require a binary search, such an approach will have an average `O[log N]` complexity where N is the number data points seen so far. As N grows, the median computation becomes very slow and real time reporting is impossible.

To obtain a scalable algorithm for the current problem, we need to consider additional structure. The key is that there are implicit constraints on median word counts. Tweets are limited to 140 characters and so the possible number of unique words that can appear in a tweet is limited. In particular, using all printable non-whitespace ASCII characters, the tweet with the highest possible unique wordcount is:

    a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~

This tweet has length 135 and contains 68 unique words (per the definitions of this challenge).  If we have two more unique characters, we can construct a valid tweet of length 139, with 70 unique words.  Thus, we can assume that the unique word count for any tweet is always an integer in the range 0 to 70 inclusive.  This additional structure allows us to produce a solution with `O[1]` space and time complexity.

The idea of the solution is to maintain a histogram of the unique word counts/per tweet for the collection of tweets seen so far.  A histogram can be represented as an array A of size 71.  Each index into A corresponds to a possible value for unique tweet word counts.  The value at the index is the number of times a tweet with that particular unique word count was observed.  From the histogram, we can compute the current median in constant time (see the Histogram class in median_unique.py for the algorithm details).  Because the size of A is constant, this algorithm also has constant space complexity.

## Distributing the computation
This solution presented so far scales very well on a single machine, however, it is not a realistic solution for a production deployment. In a real life, we'll likely distribute the work of monitoring the twitter stream to many "listeners". Suppose we have 4 computers each assigned to listen to the tweets from a certain group of users:

|Computer number|username startswith|
|---------------|-------------------|
|1|A-E|
|2|D-F|
|3|H-P|
|4|Q-Z|

How could the tools we have developed so far be extended to solve the word frequency and median problem in this distributed context?

A basic approach is to run the current set of tools on each individual computer and 
then run a "reducer" whose job is to combine the results computed across multiple systems. For word frequencies, the reducer would simply combine the word frequency dictionaries across its inputs.  For median unique word counts, the reducer would combine the unique word count histograms across its inputs.  Schematically:

    Step 1 (mapping tweets to Frequency F and Histogram H):
        Computer 1 -> F1, H1
        Computer 2 -> F2, H2
        Computer 3 -> F3, H3
        Computer 4 -> F4, H4

    Step 2 (first reduction):
        Reduce((F1,H1), (F2, H2)) -> FR1, HR1
        Reduce((F3,H3), (F4, H4)) -> FR2, HR2

    Step 3 (second reduction):
        Reduce((FR1,HR1), (FR2,HR2)) -> F,H

