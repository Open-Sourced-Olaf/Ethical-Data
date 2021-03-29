from sklearn.feature_extraction.text import CountVectorizer
import pandas
df = pandas.read_csv('google.csv')
sample_text = [df.iloc[:, 0].name]

print('\nFull dictionary of word count: \n')
dictA = dict(zip(sorted(CountVectorizer().fit(sample_text).vocabulary_.keys()), CountVectorizer(
).fit_transform(sample_text).toarray()[0]))
print(dictA)
print('\nIn decreasing order: \n')
print(sorted(dictA, key=dictA.get, reverse=True))

# Or if we wanted vectors for each word
print('\nTo and you\n')
print(CountVectorizer().fit(['some sample', 'text to you']).transform(
    ['to', 'you']).toarray())
