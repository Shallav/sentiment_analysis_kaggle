#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: sh $0 <NUMBER OF MODELS>" >&2
  exit 1
fi
echo ""
echo "Generating CSV files ...."
for (( c=1; c<=$1; c++ ))
do
   echo ""
   echo "Model $c ..."
   python generate_kaggle_submission.py ../data/Models/model$c.json $c
   echo "Model $c complete."
   echo ""
done

echo "Taking the vote and generating final submission file ...."
python compareCSV.py $1 > submission.csv

echo "Removing intermediate files ...."
for (( c=1; c<=$1; c++ ))
do
   rm submission$c.csv
done