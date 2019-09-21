import re
import urllib.request
import urllib.parse
import os
import time


# 构建请求的函数，包含User Agent
def handle_request(url1, a):
    url2 = url1 + str(a) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
    }
    request = urllib.request.Request(url=url2, headers=headers)
    return request


# 解析内容并下载图片的函数
def download_image(c):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)   # 有用的内容用小括号括起来，不用的内容就用.*?
    # < img
    # src = "//pic.qiushibaike.com/system/pictures/12222/122225712/medium/X5YUQ35PCFPYWY8D.jpg"
    # alt = "你们是不是玩不起啊" >
    lt = pattern.findall(c)
    # print(len(lt))

    # 下一步，遍历列表，处理图片链接，并下载所有图片
    for image_url in lt:
        image_url1 = 'https:' + image_url
        # 判断是否存在文件夹，如果不存在，则创建文件夹
        folder_name = 'qiutu'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        # 使用原来图片文件名作为新的文件名
        # 例：图片的url为"//pic.qiushibaike.com/system/pictures/12222/122225712/medium/X5YUQ35PCFPYWY8D.jpg"，则文件名为"X5YUQ35PCFPYWY8D.jpg"
        file_name = image_url.split('/')[-1]
        file_path = folder_name + '/' + file_name
        print('%s正在下载...' % file_name)
        # 使用retrieve方法下载文件
        urllib.request.urlretrieve(image_url1, file_path)
        print('%s已完成下载' % file_name)
        time.sleep(1)
    return


def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    page1 = int(input('请输入起始页码：'))
    page2 = int(input('请输入结束页码：'))
    for page in range(page1, page2 + 1):
        print('第%s页正在开始下载...' % page)
        # 利用写好的函数构建请求
        request = handle_request(url, page)
        # 发送请求之后获取响应
        content = urllib.request.urlopen(request).read().decode()
        # 寻找响应中的图片
        download_image(content)
        print('第%s页已经完成下载' % page)
        print()
        print()
        time.sleep(2)


if __name__ == '__main__':
    main()
