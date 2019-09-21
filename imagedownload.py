import urllib.request

# 第一种方法，urlopen
image_url = 'http://www.trytoprogram.com/images/python_bytes_function.jpg'
response = urllib.request.urlopen(image_url)
# 图片只能写入本地的二进制格式
with open('test.jpg', 'wb') as pp:
    pp.write(response.read())

# 第二种方法，urlretrieve
urllib.request.urlretrieve(image_url, 'test1.jpg')
