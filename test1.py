import urllib.request

url: str = 'http://www.baidu.com'
response = urllib.request.urlopen(url=url)
print(response.read().decode())