import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 构建handler
handler = urllib.request.HTTPHandler()
# 构建opener
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url=url, headers=headers)
response = opener.open(request)

print(response.read().decode())
