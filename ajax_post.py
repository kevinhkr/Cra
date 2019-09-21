import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword '

city = input('请输入您想查询的城市：')
page_number = input('请输入您想要的页码：')
page_size = input('请输入每页显示的数量：')

form_data = {
    'cname': city,
    'pid': '',
    'keyword':	'',
    'pageIndex':	page_number,
    'pageSize':	page_size,
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
