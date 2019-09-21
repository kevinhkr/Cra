import urllib.request
import urllib.parse
import os

# 目标：输入指定吧名，并输入要爬取的起始页和结束页，创建一个名为吧名的文件夹，并将爬取的html文件以吧名_page.html为文件名放入文件夹

url = 'http://tieba.baidu.com/f?ie=utf-8'
name = input('请输入吧名：')
page_start = int(input('请输入起始页码：'))
page_end = int(input('请输入结束页码：'))

if not os.path.isdir(name):
    os.mkdir(name)   # 如果目录下没有这个名字命名的文件夹，生成名为吧名的文件夹

for page in range(page_start, page_end + 1):
    # page是当前页
    data = {
        'kw': name,
        'pn': (page-1)*50,
    }

    query_string = urllib.parse.urlencode(data)
    new_url = url + query_string
    print('正在下载第%s页……' % page)
    response = urllib.request.urlopen(new_url)

    file_name = name + '_' + str(page) + '.html'   # 生成文件名
    file_path = name + '/' + file_name   # 生成文件路径

    with open(file_path, 'wb') as fp:
        fp.write(response.read())

    print('已完成下载第%s页……' % page)
