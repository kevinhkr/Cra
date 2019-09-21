import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action='
page = int(input('The page you want to view: '))
number = 20   # 每页显示个数
data = {
    'start': (page-1) * number,
    'limit': number,
}   # 构建get参数
query_string = urllib.parse.urlencode(data)   # 将字典转化为合法query_string
url += query_string   # 构建完整请求url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 构建请求对象“request”
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode())

