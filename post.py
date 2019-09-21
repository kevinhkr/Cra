import urllib.request
import urllib.parse
import json
# 获取posturl的地址
post_url = 'https://fanyi.baidu.com/sug'
#word = input('Please type in the word you want to translate: ')
# 构建post表单数据，写成字典
form_data = {
    'kw': "baby",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 处理post表单数据，并变成字节类型（原先是字符串类型）
form_data = urllib.parse.urlencode(form_data).encode()
# 构建请求对象“request”
request = urllib.request.Request(url=post_url, headers=headers)
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())
