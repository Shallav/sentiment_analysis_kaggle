"""
Generate a tsv submission file to kaggle's 'Sentiment Analysis on Movie Reviews' (samr)
competition using the samr module with a given json configuration file.
"""


def fix_json_dict(config):
    new = {}
    for key, value in config.items():
        if isinstance(value, dict):
            value = fix_json_dict(value)
        elif isinstance(value, str):
            if value == "true":
                value = True
            elif value == "false":
                value = False
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass
        new[key] = value
    return new


if __name__ == "__main__":
    import argparse
    import json
    import csv

    from samr.corpus import iter_corpus, iter_test_corpus
    from samr.predictor import PhraseSentimentPredictor
     
    trainFile = 'train_mini.tsv'
    testFile = 'test_mini.tsv'

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename")
    parser.add_argument("numModel")
    config = parser.parse_args()
    numModel = config.numModel
    config = json.load(open(config.filename))

    predictor = PhraseSentimentPredictor(**config)
    predictor.fit(list(iter_corpus(trainFile)))
    test = list(iter_test_corpus(testFile))
    prediction = predictor.predict(test)

    # writer = csv.writer(sys.stdout)
    # writer.writerow(("PhraseId", "Sentiment"))
    # for datapoint, sentiment in zip(test, prediction):
    #     writer.writerow((datapoint.phraseid, sentiment))

    outFile = 'submission' + str(numModel) + '.csv'
    output = open(outFile, 'wb')
    writer = csv.writer(output)
    writer.writerow(("PhraseId", "Sentiment"))
    for datapoint, sentiment in zip(test, prediction):
        writer.writerow((datapoint.phraseid, sentiment))
    output.close()
