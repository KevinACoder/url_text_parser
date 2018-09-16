import requests
from collections import Counter

def download_file(url):
	req = requests.get(url)
	if req.status_code == 404:
		print('url not exist')
		return '', False

	return req.content, True

def create_local_file(raw, save_path):
	with open(save_path, 'wb') as file:
		file.write(raw)
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

def export_result(occurance, export_path, num):
	sorted_item = []
	count = 0
	for item, times in occurance.most_common(num)[:]:
		if count < 10:
			sorted_item.append(item + "\r\n")
			print(item)
			count += 1;

	export = ''.join(sorted_item)
	with open(export_path, 'wb') as file:
		file.write(export.encode('utf-8'))
	return