import implement as imp

def test_url_download():
	urls = ['https://github.com/KevinACoder/url_text_parser/raw/master/file_remote.txt',
	'https://github.com/KevinACoder/url_text_parser/raw/master/file_remote_small.txt',
	'https://not_exist_file.txt',
	'https://github.com/KevinACoder/url_text_parser/raw/master/not_text.jpg']

	for url in urls:
		raw_data, state = imp.download_file(url)
		if state == False:
			print('fail')

	return

def test_file_copy():
	local_path = './file_local_test.txt'
	raw_data = 'Hello world\n Hello Python'
	imp.create_local_file(raw_data, local_path)
	return

def test_col_extract():
	local_path = './file_local_test.txt'
	items = imp.extract_cols(local_path, 2)
	return

def test_sorting():
	items = ['Hello', 'world', 'Hello', 'Python']
	occurance = imp.count_item(items)
	print(occurance.most_common(10))
	return

def test_result_export():
	export_path = './result_test.txt'
	occurance = [('Hello', 2), ('world', 1), ('Python', 1)]
	imp.export_result(occurance, export_path)
	return


test_url_download()
test_file_copy()
test_col_extract()
test_sorting() 
test_result_export()