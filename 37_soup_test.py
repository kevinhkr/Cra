from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs_test.html'), 'lxml')
# soup的类型是一个对象，但是使用print函数时会输出字符串

# print(soup)

# print(soup.li)   # 通过标签名去找html中的字符串，但是只能找到第一个，

# print(soup.ol['class'])   # 调出指定属性
# print(soup.ol['style'])
# print(soup.ol.attrs)   # 调出所有属性，返回字典
# print(soup.ol.attrs['class'])   # 跟上面soup.ol['class']相同

# print(soup.ol.text)   # 获取标签里所有内容
# print(soup.li.string)   # 如果标签内没有别的标签，获取内容，如果还有别的标签，返回None
# print(soup.ol.get_text())

# print(soup.find('ol'))
# print(soup.find('ol', title='bbb'))

# print(soup.find_all('ol'))
# print(soup.find_all(['a', 'b', 'f']))   # 找到所有列表中的标签
# print(soup.find_all('ol', limit=2))   # 找到前两个符合要求的标签

print(soup.select('ol > a'))
