import implement as imp

url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
raw_data = imp.download_file(url)
print('downloaded')
local_path = './file_local.txt'
imp.create_local_file(raw_data, local_path)
print('cp to local')
items = imp.extract_cols(local_path, 2)
print('extract specific col')
occurance = imp.count_item(items)
print(occurance.most_common(10))
print('count occurance')
export_path = './result.txt'
imp.export_result(occurance, export_path)
print('result exported')