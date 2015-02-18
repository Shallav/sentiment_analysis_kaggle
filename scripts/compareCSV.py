import csv
import sys
from collections import Counter

numModels = 0
test = []
submission = []
def create_phraseID_sentiment_lists(csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            test.append(row[0])
            submission.append([int(row[1])])
    return

def create_sentiment_lists(csv_file):
    '''make a dictionary from all csv files'''
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        i = 0
        for row in reader:
            submission[i].append(int(row[1]))
            i = i + 1
    return

def take_vote():
    j = 0
    for i in submission:
        count = Counter(i)
        submission[j] = str(count.most_common()[0][0])
        j = j + 1

def create_final_submission():
    writer = csv.writer(sys.stdout)
    writer.writerow(("PhraseId", "Sentiment"))
    for datapoint, sentiment in zip(test, submission):
        writer.writerow((datapoint, sentiment[0]))


def main():
    create_phraseID_sentiment_lists('submission1.csv')
    for i in range(2, numModels + 1):
        filename = 'submission' + str(i) + '.csv' 
        create_sentiment_lists(filename)

    take_vote()
    create_final_submission()
    
if __name__ == '__main__':  
    numModels = int(sys.argv[1]) 
    main()