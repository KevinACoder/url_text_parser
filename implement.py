import requests

#downloading text file 
#https://stackoverflow.com/questions/50117238/how-to-download-text-file-from-url-and-save-it-in-django-project-directory
example_txt = 'https://github.com/KevinACoder/url_text_parser/blob/master/file_remote.txt'
r = requests.get(example_txt)
with open('./file_local.txt', 'wb') as f:
    f.write(r.content)

