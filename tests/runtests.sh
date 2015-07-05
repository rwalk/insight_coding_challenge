export PYTHONPATH=..

echo "Running Python unit tests..."
python3 unit_tests.py

echo "Running scalability tests..."
python3 scalability_tests.py

echo "Running end to end tests..."
for f in test1 test2 test3
do
    python3 ../src/words_tweeted.py data/$f/tweets_input/tweets.txt data/$f/tweets_output/ft1.txt
    python3 ../src/median_unique.py data/$f/tweets_input/tweets.txt data/$f/tweets_output/ft2.txt
    t1=$(diff -w data/$f/tweets_output/ft1.txt data/$f/expected/ft1.txt | wc -l)
    if (($t1 -ne -0))
    then 
        echo "FAILED e2e $f part 1" 
    else 
        echo "PASSED e2e $f part 1" 
    fi
    t2=$(diff -w data/$f/tweets_output/ft1.txt data/$f/expected/ft1.txt | wc -l)
    if (($t2 -ne -0))
    then
        echo "FAILED e2e $f part 2"
    else
        echo "PASSED e2e $f part 2"
    fi
done



