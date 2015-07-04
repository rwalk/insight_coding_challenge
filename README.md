Insight Data Engineering - Coding Challenge [Solution]
===========================================================

In the most general setting, computing the median is difficult to scale.  One approach
would be to maintain the data in sorted order and track the middle element.  Since
each insert into the sorted list would require binary search, such an
approach would cost O(log N) where N is the number data points.  Clearly, this
won't scale.

In this problem, however, we can take advantage of the fact that a tweet can have
at most 140 characters.  In particular, using all printable non-whitespace ASCII characters, the tweet with the highest possible unique wordcount is:

    a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~

This tweet has length 135 and contains 68 unique words (per the rules of this challenge).  If we have two more unique characters, we can construct a valid tweet of length 139, with 70 unique words.  So 70 is the largest possible unique word count for a tweet.  This fact can allow us to compute the running median in constant time.  


Here is the approach:

0) Allocate an array $A$ of length 70 to track occurences of unique tweet word counts.  Initialize each entry of the array to 0.
1) For each tweet, compute $c$ count the number of unique words in the array.  Note that $0 \leq c \leq 70$.  
2) Increment $A[c]$ by 1.
1) Compute $N = \sum_{i=0}^{70} A[i]$ which is the number of tweets observed so far.
2) If N is odd, the median is the value at N/2 (0 indexing). If N is odd, the median is the mean of values at N/2, N/2 - 1 (0 indexing).
