import urllib.request
import urllib.parse
import time
import re
import os

# 要求：爬取指定页面的标题和内容，保存到html文件中
# 标题使用h1格式，内容使用p格式


def handle_request(a, b=None):
    if b is not None:
        url1 = a + str(b) + '.html'
    else:
        url1 = a
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
    }
    request = urllib.request.Request(url=url1, headers=headers)
    return request


def download_text(src, title):
    request = handle_request(src)
    response = urllib.request.urlopen(request).read().decode()
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    # <li><p>请再努力一下，为了你想见的人，想做的事，想成为的自己。<br></p></li>
    ret = pattern.findall(response)
    text = ret[0]
    # 写个正则，将内容里的图片去掉，只留下文字
    pattern2 = re.compile(r'<p><img .*?><br/></p>', re.S)
    # <p><img title="271564239406318612.jpeg" alt="20140915144801_BWfNw.thumb.700_0.jpeg" src="/uploads/image/201907/271564239406318612.jpeg"><br></p>
    ret1 = pattern2.sub('', text)
    # print(ret1)
    return ret1


def analyse_text(c):
    pattern = re.compile(r'<div class="art-t">.*?<a href="(.*?)"><b>(.*?)</b>.*?</div>', re.S)
    # <div class="art-t"> <h3><a href="/lizhi/qianming/20190841364.html"><b>愿有前程可奔赴，亦有岁月可回首——前程似锦要靠自己打拼</b></a></h3> <p>在自己身上，克服这个时代。 既然今天，没人识得星星一颗，那么明日，何妨做皓月一轮 人一辈子都在高潮和低潮中浮沉，唯有庸碌的人，生活才如死水一般。 有时候你以为天要塌下... </p> </div>
    # 返回的ret是一个列表，列表中的元素都是元组，元组中的第一个元素是正则中第一个括号匹配到的内容，第二个元素是正则中第二个匹配到的内容
    ret = pattern.findall(c)
    for group in ret:
        # 获取内容的链接
        src = 'http://www.yikexun.cn' + group[0]
        # 获取内容的标题
        title = group[1]
        text = download_text(src, title)
        string = '<h1>%s</h1>%s' % (title, text)
        with open('lizhi.html', 'a', encoding='gbk') as fp:
            fp.write(string)
    pass


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    page1 = int(input('请输入起始页码：'))
    page2 = int(input('请输入结束页码：'))
    for page in range(page1, page2 + 1):
        print('第%s页正在开始下载...' % page)
        # 利用写好的函数构建请求
        request = handle_request(url, page)
        # 发送请求之后获取响应
        content = urllib.request.urlopen(request).read().decode()
        # 寻找响应中的图片
        analyse_text(content)
        print('第%s页已经完成下载' % page)
        print()
        print()
        time.sleep(2)
    pass


if __name__ == '__main__':
    main()
