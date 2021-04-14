import numpy as np
import pandas as pd
import sklearn.model_selection as sm
import csv
import fasttext
from gensim.utils import simple_preprocess

newDataSetVersion = pd.read_csv('policy_train_data.csv')[
    ['Query', 'Label', 'Segment']]

newDataSetVersion['category'] = newDataSetVersion['Query'] + ' ' + \
    newDataSetVersion['Label']

newDataSetVersion = newDataSetVersion[['Segment', 'category']].rename(
    columns={'Segment': 'questions', 'category': 'category'})

newDataSetVersion['category'] = newDataSetVersion['category'].str.replace(
    ' ', '_')

train, test = sm.train_test_split(
    newDataSetVersion, test_size=0.4, shuffle=True, random_state=42)

train.iloc[:, 0] = train.iloc[:, 0].apply(
    lambda x: ' '.join(simple_preprocess(x)))
test.iloc[:, 0] = test.iloc[:, 0].apply(
    lambda x: ' '.join(simple_preprocess(x)))

train.iloc[:, 1] = train.iloc[:, 1].apply(lambda x: '__label__' + x)
test.iloc[:, 1] = test.iloc[:, 1].apply(lambda x: '__label__' + x)

train[['category', 'questions']].to_csv('train.txt',
                                        index=False,
                                        sep=' ',
                                        header=None,
                                        quoting=csv.QUOTE_NONE,
                                        quotechar="",
                                        escapechar=" ")

test[['category', 'questions']].to_csv('test.txt',
                                       index=False,
                                       sep=' ',
                                       header=None,
                                       quoting=csv.QUOTE_NONE,
                                       quotechar="",
                                       escapechar=" ")

model = fasttext.train_supervised('train.txt', wordNgrams=10)

print(model.test('test.txt'))

print(model.predict(test.iloc[1, 0]))
print(test.iloc[1, 0])

model.save_model('model.bin')
