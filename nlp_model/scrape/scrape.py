import csv
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import json


def scrape_google(url):

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


def scrape_twitter(url):

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
    clean_text = filter(None, clean_text)
    text = ' '.join(clean_text)

    # Put results into a dictionary
    result = {'text': text}
    return result


def scrape_amazon(url):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # All of the text is in <p> tags, so get all the <p> tags
    all_p_tags = soup.find_all('p')
    all_list_tags = soup.find_all('li')
    clean_text = []

    # Iterate through all the <p> tags and add them to an array
    for sentence in all_p_tags:
        # Remove <p> tags from the string, only keep contents with .text
        clean_text.append(sentence.text)

    for sentence in all_list_tags:
        clean_text.append(sentence.text)

    # Combine all elements in clean_text array into a single string

    clean_text = filter(None, clean_text)
    text = ' '.join(clean_text)

    # Put results into a dictionary
    result = {'text': text}
    return result


def scrape_microsoft(url):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # All of the text is in <p> tags, so get all the <p> tags
    all_p_tags = soup.find_all('p')
    all_list_tags = soup.find_all('li')
    clean_text = []

    # Iterate through all the <p> tags and add them to an array
    for sentence in all_p_tags:
        # Remove <p> tags from the string, only keep contents with .text
        clean_text.append(sentence.text)

    for sentence in all_list_tags:
        clean_text.append(sentence.text)

    # Combine all elements in clean_text array into a single string
    clean_text = filter(None, clean_text)
    text = ' '.join(clean_text)

    # Put results into a dictionary
    result = {'text': text}
    return result


if __name__ == '__main__':
    scrapedText = scrape_google("https://policies.google.com/privacy")
    with open('google.csv', 'w+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([scrapedText['text']])

    scrapedText = scrape_twitter('https://twitter.com/en/privacy')
    print(scrapedText)
    with open('twitter.csv', 'w+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([scrapedText['text']])

    # Amazon detected I'm scraping so I got a 503
    # scrapedText = scrape_amazon('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')
    # with open('amazon.csv', 'w+', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow([scrapedText['text']])

    scrapedText = scrape_microsoft(
        'https://privacy.microsoft.com/en-ca/privacystatement')
    print(scrapedText)
    with open('microsoft.csv', 'w+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([scrapedText['text']])
