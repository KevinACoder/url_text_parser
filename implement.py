import requests

example_txt = 'http://www.textfiles.com/100/914bbs.txt'

r = requests.get(example_txt)
with open('./file.txt', 'wb') as f:
    f.write(r.content)