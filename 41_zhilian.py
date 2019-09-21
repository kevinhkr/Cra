import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


class ZhilianSpider(object):
    url = 'https://sou.zhaopin.com/?'

    def __init__(self, city, kw, sp, ep):
        # 将上面的参数都保存为自己的成员属性
        self.jl = city
        self.kw = kw
        self.sp = sp
        self.ep = ep
        pass

    def handle_request(self, page):   # 根据信息生成访问的url，并构建请求
        query_string = {
            'p': page,
            'jl': self.jl,
            'kw': self.kw,
        }
        string = urllib.parse.urlencode(query_string)
        final_url = self.url + string
        # print(final_url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        request = urllib.request.Request(url=final_url, headers=headers)
        return request

    def parse(self, content):   # 解析内容
        # soup = BeautifulSoup(content, 'lxml')   # 生成对象
        # 思路；先找到所有“div class="contentpile__content__wrapper__item clearfix"”，一个工作岗位就是一个这个玩意儿，然后通过这个对象的find、select方法去寻找没一条记录里的信息
        # div_list = soup.select('.contentpile')
        soup = BeautifulSoup(open('zhilian_test.html'), 'lxml')
        div_list = soup.select('#listContent > .contentpile__content__wrapper clearfix')
        print(div_list)
        print(len(div_list))

    def run(self):   # 总程序
        for page in range(self.sp, self.ep+1):
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode()
            # print(content)
            # 解析内容
            self.parse(content)


def main():
    city = input('请输入您想查询的城市：')
    kw = input('请输入工作关键字：')
    sp = int(input('请输入起始页码：'))
    ep = int(input('请输入结束页码：'))
    # 创建对象，启动爬取程序
    spider = ZhilianSpider(city, kw, sp, ep)
    spider.run()
    pass


if __name__ == '__main__':
    main()
