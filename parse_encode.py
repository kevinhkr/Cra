import urllib.request
import urllib.parse

word = input('What do you want to search in Baidu: ')
url = 'http://www.baidu.com/s?'
data = {
    'ie': 'utf-8',
    'wd': word,
}
query_string = urllib.parse.urlencode(data)
url += query_string

response = urllib.request.urlopen(url)
name = word + '.html'
with open(name, 'wb') as pp:
    pp.write(response.read())
