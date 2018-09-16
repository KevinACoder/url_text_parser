import implement as imp

#0. user configs
url = 'https://github.com/KevinACoder/url_text_parser/raw/master/file_remote.txt'
local_path = './file_local.txt'
target_col = 2
export_path = './result.txt'
export_result_num = 20

#1. download url file
raw_data, state = imp.download_file(url)
print(type(raw_data))
if state == False:
	exit('exit... download url file fail !!')
print('1. downloaded')

#2. create file in hard-disk
imp.create_local_file(raw_data, local_path)
print('2. cp to local')

#3. extract target col words in file
items = imp.extract_cols(local_path, target_col)
print('3. extract specific col')

#4. count frequency of words
occurance = imp.count_item(items)
print('4. count occurance, result as following')
print(occurance.most_common(export_result_num))

#5. export result to text file
imp.export_result(occurance, export_path, export_result_num)
print('5. result exported to ', export_path)