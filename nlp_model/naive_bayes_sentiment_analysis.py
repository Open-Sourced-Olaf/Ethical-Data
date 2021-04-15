import pandas
import re
import csv

fh = open("dataset.csv", "r")

reader = csv.reader(fh, delimiter='+')

label_word = {}
label_records = {}
word_label = {}

for row in reader:
    label_records.setdefault(row[1], 0)
    label_word.setdefault(row[1], {})
    # label_records counts records of each label, row[1] is the label
    label_records[row[1]] += 1
    # row[0] is the sentence, row[1] is the label
    split_data = re.split('[^a-zA-Z\']', row[0])
    for i in split_data:
        if len(i) > 2:  # if the word length is greater than 2
            # label_word's default is { label : { word : 0 } }
            label_word[row[1]].setdefault(i.lower(), 0)
            word_label.setdefault(i.lower(), {})
            # word_label's default is { word : { label : 0 } }
            word_label[i.lower()].setdefault(row[1], 0)
            label_word[row[1]][i.lower()] += 1
            word_label[i.lower()][row[1]] += 1


def probability_of_observing_test_data_given_category(text, category):
    split_data = re.split('[^a-zA-Z][\'][ ]', text)
    data = []
    for i in split_data:
        if ' ' in i:
            i = i.split(' ')
            for j in i:
                if j not in data:
                    data.append(j.lower())
        elif len(i) > 2 and i not in data:
            data.append(i.lower())
    p = 0
    for word in data:
        # weighted probability of a word for a category
        basic_prob = 0
        total_number_of_appearances = 0
        if word in word_label and word in label_word[category]:
            basic_prob = float(label_word[category]
                               [word]) / label_records[category]
        if word in word_label:
            total_number_of_appearances = sum(word_label[word].values())
        else:
            total_number_of_appearances = 0
        weight_prob = (0.5 + (total_number_of_appearances * basic_prob)
                       ) / (1.0+total_number_of_appearances)
        p += weight_prob
    return p


def naive_bayes(text):
    '''
    p(A|B) = p(B|A) * p(A) / p(B)
        A: Category
        B: Test data
        p(A|B): Category given the Test data
    We don't have to calculate p(B) because we already have test data so
    p(B) remains constant for every category.  We can directly compare the
    numerators and predict the class accordingly.
    '''
    results = {}
    for i in label_word.keys():
        A = float(label_records[i]) / sum(label_records.values())
<<<<<<< HEAD
        BgivenA = probability_of_observing_test_data_given_category(text, i)
        results[i] = BgivenA*A
=======
        B = probability_of_observing_test_data_given_category(text, i)
        results[i] = B*A
>>>>>>> 7ea0cadc35cda61b4656454729c3d05db7d4625c
    return results


df = pandas.read_csv('./scrape/google.csv')
sample_text = df.iloc[:, 0].name
result = naive_bayes(sample_text)
print(result)

for x in ['data_collected', 'primary_usage', 'privacy',
          'improper_access', 'personal_information', 'usage_information', 'data_usage']:
    if (
        (x in result.keys())
        and
        (('-' + x) in result.keys())
        and
        (result[x] > result['-' + x])
    ):
        print(x)
    else:
        print('-' + x)
