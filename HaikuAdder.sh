for i in {1..$3}; do
	python NLTKStatsModel.py $1 $2 >> haikus.csv
done