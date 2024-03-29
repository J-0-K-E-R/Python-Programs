import requests
from bs4 import BeautifulSoup
import operator


def start(url):                                                     # This will grab the data from the web page
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for post_text in soup.findAll('p'):
        con = str(post_text).replace("<br>", "\n")
        clear_con = BeautifulSoup(con, "html.parser")
        content = clear_con.get_text()
        words = content.lower().split()                             # Making content lower case and splitting by space to get each word.
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):                                      # It'll clean up our text and remove the extra symbols.
    clean_list = []
    for each_word in word_list:
        symbols = "~!@#$%^&*()_+=-`{}|:\"<>?[]\;',./'"             # List of symbols that it'll remove from words.
        for i in range(0, len(symbols)):
            each_word = each_word.replace(symbols[i], "")
        if len(each_word) > 0:
            clean_list.append(each_word)
    counter(clean_list)


def counter(word_list):                                           # Counting the frequency of each word.
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("'" + str(key) + "' occurs " + str(value) + " times.")


# URL from where we want to scrap the information.
URL = "https://en.wikipedia.org/wiki/Death_Note"

start(URL)