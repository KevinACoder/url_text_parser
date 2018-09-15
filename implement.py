import requests
from urllib import request
import nltk, re, pprint
from nltk import word_tokenize
from collections import Counter

def url_is_alive(url):
    req = request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        request.urlopen(req)
        return True
    except request.HTTPError:
        return False

def download_file(url):
	if url_is_alive(url) == False :
		print('url not exist')
		return

	raw = requests.get(url)
	return raw

def create_local_file(raw, save_path):
	with open(save_path, 'wb') as file:
		file.write(raw.encode('utf-8'))
	return

def extract_cols(save_path, col_ix):
	items = []
	count = 0
	with open(save_path, 'r') as file:
		for line in file:
			words = line.split(" ")
			if len(words) > col_ix:
				items.append(words[col_ix])
				count += 1
	return items

def count_item(items):
	occurance = Counter(items)
	return occurance

def export_result(occurance, export_path):
	sorted_item = []
	count = 0
	for item, times in occurance.most_common()[:]:
		if count < 10:
			sorted_item.append(item + "\r\n")
			print(item)
			count += 1;

	#export = 'occurance of items\n\r'
	export = ''.join(sorted_item)
	#print(type(export))
	#print(export)
	with open(export_path, 'wb') as file:
		file.write(export.encode('utf-8'))
	return

# url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
# raw_data = download_file(url)
# print('downloaded')
# local_path = './file_local.txt'
# create_local_file(raw_data, local_path)
# print('cp to local')
# items = extract_cols(local_path, 2)
# print('extract specific col')
# occurance = count_item(items)
# print(occurance.most_common(10))
# print('count occurance')
#downloading text file 
#https://stackoverflow.com/questions/50117238/how-to-download-text-file-from-url-and-save-it-in-django-project-directory
#example_txt = 'http://www.gutenberg.org/files/2554/2554-0.txt'#'https://github.com/KevinACoder/url_text_parser/blob/master/file_remote.txt'
#r = requests.get(example_txt)
#with open('./file_local.txt', 'wb') as f:
#    f.write(r.content)

#file = open('./file_local.txt', 'r')
#third_items = []
#count = 0
#for line in file:
#	words = line.split(" ")
#	if count<10 and len(words) >= 3:
#		print(words[2])
#		third_items.append(words[2])
#	count += 1

#occurance = Counter(third_items)
#print('lines: ', count, ' ', third_items[0], ':', occurance[third_items[0]])
#print(occurance.most_common(10))