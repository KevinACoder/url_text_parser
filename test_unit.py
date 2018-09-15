import implement as imp

def test_url_download():
	url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
	raw_data = imp.download_file(url)
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

#case 1: network is reachable, url valid
#2: network is reachable, url invalid
#3: network not reachable
#test_url_download()

#case 1: target file not yet created
#2: target file exist
#3: max size of content can be load to save to file
#4: encoding, need to support unicode or not
#test_file_copy()

#case 1: target file exist, target col valid
#2: 
test_col_extract()