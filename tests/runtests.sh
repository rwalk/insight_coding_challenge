export PYTHONPATH=..

echo "Running Python unit tests..."
python3 unit_tests.py

echo "Running scalability tests..."
python3 scalability_tests.py

echo "Running end to end tests..."
python3 ../src/words_tweeted.py data/test1/tweets_input/tweets.txt data/test1/tweets_output/ft1.txt
python3 ../src/median_unique.py data/test1/tweets_input/tweets.txt data/test1/tweets_output/ft2.txt
t1=$(diff -w data/test1/tweets_output/ft1.txt data/test1/expected/ft1.txt | wc -l)
if (($t1 -ne -0))
then 
    echo "FAILED e2e test 1" 
else 
    echo "PASSED e2e test 1" 
fi

t2=$(diff -w data/test1/tweets_output/ft2.txt data/test1/expected/ft2.txt | wc -l)
if (($t2 -ne -0))
then
    echo "FAILED e2e test 2"
else
    echo "PASSED e2e test 2"
fi




