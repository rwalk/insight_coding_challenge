Insight Data Engineering - Coding Challenge [Solution]
===========================================================



# Solution description

## Counting words for tweets
Using a key-value dictionary, it is straightforward to implement an $\mathcal{O}(1)$ time complexity word counter.
When a new tweet arrives, we take each word and check if it is present in the dictionary.  If it's not found,
we add the word as new key in the dictionary and set the value to 1.  If the word is already in the dictionary, we increment its value by 1.
Since dictionaries provide average amortized constant-time lookup and insert, this solution is $\mathcal{O}(1)$ in time.  In terms of space complexity, the dictionary size will be proportional to the vocabulary of all the tweets recieved so far.  


## Tweet rolling median words per tweet
In general, computation of a median does not scale well.  One approach is to maintain 
the data in sorted order and track the middle element.  Since each insert into the sorted 
list requires a binary search, such an approach has an average $\mathcal{O}(\mathcal{log} N)$ complexity where N is the number data points
seen so far.  For very large $N$, such an approach is impractical, particularly if we need to report medians in real time.

In this problem, however, a simple and scalable solution is possible once we recognize that tweets are limited to 140 characters. In particular, using all printable non-whitespace ASCII characters, the tweet with the highest possible unique wordcount is:

    a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~

This tweet has length 135 and contains 68 unique words (per the rules of this challenge).  If we have two more unique characters, we can construct a valid tweet of length 139, with 70 unique words.  Thus, we can assume that the unique word count for any tweet is always an integer in the range $0$ to $70$ inclusive.  This fact is sufficient to obtain an $\mathcal{O}(1)$ solution in space and time.

Here is the approach:

0) Allocate an array $A$ of length 70 to track occurences of unique tweet word counts.  Initialize each entry of the array to 0.
1) For each tweet, compute $c$ count the number of unique words in the array.  Note that $0 \leq c \leq 70$.  
2) Increment $A[c]$ by 1.
1) Compute $N = \sum_{i=0}^{70} A[i]$ which is the number of tweets observed so far.
2) If N is odd, the median is the value at N/2 (0 indexing). If N is odd, the median is the mean of values at N/2, N/2 - 1 (0 indexing).
