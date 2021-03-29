import csv
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import json


def scrape(url):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # All of the text is in <p> tags, so get all the <p> tags
    all_text = soup.find_all('p')
    clean_text = []

    # Iterate through all the <p> tags and add them to an array
    for sentence in all_text:
        # Remove <p> tags from the string, only keep contents with .text
        clean_text.append(sentence.text)

    # Combine all elements in clean_text array into a single string
    text = ' '.join(clean_text)

    # Put results into a dictionary
    result = {'text': text}
    return result


if __name__ == '__main__':
    scrapedText = scrape("https://policies.google.com/privacy")
    print(scrapedText)
    with open('google.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([scrapedText['text']])
