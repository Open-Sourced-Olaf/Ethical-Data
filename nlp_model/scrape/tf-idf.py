from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

df = pandas.read_csv('google.csv')
sample_text = df.iloc[:, 0].name

tfidf = TfidfVectorizer()
response = tfidf.fit_transform([sample_text])
feature_names = tfidf.get_feature_names()

tfIdf = {}
for col in response.nonzero()[1]:
    tfIdf[feature_names[col]] = response[0, col]

print(dict(sorted(tfIdf.items(), key=lambda item: item[1], reverse=True)))
