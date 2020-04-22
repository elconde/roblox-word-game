"""Download words_alpha.txt and get all words with at least three
letters"""
import urllib.request

URL = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'

print('Downloading', URL)
urllib.request.urlretrieve(URL, 'words-alpha.txt')
print('Done!')