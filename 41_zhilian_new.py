import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
import re

class ZhilianSpider(object):
    # url = ['https://fe-api.zhaopin.com/c/i/sou?start=', '&pageSize=90&cityId=', '&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=', '&kt=3&=0&_v=0.23683522&x-zp-page-request-id=405e345de3514a1f8d628939b13a7e89-1568992371374-72569&x-zp-client-id=a037821f-6f6f-44c9-9299-87635ca29bc2']
    url = 'https://fe-api.zhaopin.com/c/i/sou?'
    # start=0&pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&_v=0.99485895&x-zp-page-request-id=e4aff6ff312b4a0b919fe4347aea8b8a-1568992121477-946620&x-zp-client-id=a037821f-6f6f-44c9-9299-87635ca29bc2

    def __init__(self, city, kw, sp, ep):
        # 将上面的参数都保存为自己的成员属性
        self.jl = city
        self.kw = kw
        self.sp = sp
        self.ep = ep
        pass

    def handle_request(self, page):   # 根据信息生成访问的url，并构建请求
        query_string = {
            'start': str((page-1)*90),
            'pageSize': '90',
            'cityId': self.jl,
            'salary': '0,0',
            'workExperience': '-1',
            'education': '-1',
            'companyType': '-1',
            'employmentType': '-1',
            'jobWelfareTag': '-1',
            'kw': self.kw,
            'kt': '3%=0',
            '_v': '0.99485895&x-zp-page-request-id=e4aff6ff312b4a0b919fe4347aea8b8a-1568992121477-946620&x-zp-client-id=a037821f-6f6f-44c9-9299-87635ca29bc2',
        }
        final_url = self.url + urllib.parse.urlencode(query_string)
        print(final_url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        request = urllib.request.Request(url=final_url, headers=headers)
        return request

    def parse(self, content):   # 解析内容
        # {"number":"CC470484620J00373351707","jobName":"清洁工/PA员","company":{"name":"广东嘉福国际大酒店有限公司","number":"CZ470484620","type":{"name":"合资"},   "size":{"name":"100-499人"},"url":"https://company.zhaopin.com/CZ470484620.htm"},"city":{"items":[{"name":"广州","code":"763"}],"display":"广州"},"updateDate":"2019-09-18 10:20:14","salary":"3K-4.5K","distance":0,"eduLevel":{"name":"学历不限"},"jobType":{"items":[{"name":"社区/居民/家政服务"}]},"feedbackRation":1,"workingExp":{"name":"1-3年"},"industry":"200600","emplType":"全职","applyType":"1","saleType":false,"positionURL":"https://jobs.zhaopin.com/CC470484620J00373351707.htm","companyLogo":"https://fileihr.zhaopin.com/047/048/047048462/logo/a85e609a-1dcd-4d5f-bcda-7fa2f210c787.jpg","tags":[],"expandCount":0,"score":"492","vipLevel":1003,"positionLabel":"{\"chatWindow\":null,\"refreshLevel\":0,\"skillLabel\":[]}","bestEmployerLabel":[],"welfare":[],"businessArea":"建设","futureJob":false,"futureJobUrl":"","tagIntHighend":0,"rootOrgId":47048462,"staffId":1021103540,"chatWindow":1,"selected":false,"applied":false,"collected":false,"isShow":false,"timeState":"招聘中","rate":"100%"}
        pattern = re.compile(r'{"number":(.*?)"rate":".*?"}')
        lt = pattern.findall(content)
        print(lt)
        print(type(lt))
        print(len(lt))
        for job in lt:
            pattern_jobname = re.compile(r'"jobName":"(.*?)"')
            jobname = pattern_jobname.findall(job)[0]
            print(jobname)

    def run(self):   # 总程序
        for page in range(self.sp, self.ep+1):
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode()
            # print(content)
            # print(type(content))
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


time.sleep(1)

if __name__ == '__main__':
    main()
