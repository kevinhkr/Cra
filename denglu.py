import urllib.request
import urllib.parse
import http.cookiejar

# 真实地模拟浏览器，发送完post请求之后，将cookie保存到代码中
cj = http.cookiejar.CookieJar()   # 创建cookiejar
handler = urllib.request.HTTPCookieProcessor(cj)   # 根据cookiejar创建handler
opener = urllib.request.build_opener(handler)   # 根据handler创建opener，并且之后打开url都用opener的方法

url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019851156261'
form_data = {
    'email':	'18988635520',
    'origURL':	'http://www.renren.com/home',
    'domain':	'renren.com',
    'key_id':	'1',
    'captcha_type':	'web_login',
    'password':	'654a3ec450bb9bf3ded108016386d48324773d220aac035137266f25c8a0e1af',
    'rkey':	'7200822b407ccb34baa851f7a0fa9364',
    'f':	'http%3A%2F%2Fwww.renren.com%2F972181998%2Fnewsfeed%2Fphoto',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

formdata = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url=url, headers=headers)
response = opener.open(request, data=formdata)   # 登陆成功后正确的cookie会保存在opener中
print(response.read().decode())   # 显示登陆是否成功
print('*' * 50)   # 分隔行

new_url = 'http://www.renren.com/972181998/profile'
request1 = urllib.request.Request(url=new_url, headers=headers)
response1 = opener.open(request1)
print(response1.read().decode())
