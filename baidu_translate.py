import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
word = 'wolf'
form_data = {
    'from': 'en',      # 从英文
    'query': word,    # 查询的单词
        'simple_means_flag':	'3',
    'to':	'zh',        # 到中文
    'token':	'ead4daf89edeb37431315e0835720eb6',
    'transtype':	'realtime',   # 加密措施
    'sign':	'275695.55262',   # 加密措施
}

headers = {
    # 'Host': 'fanyi.baidu.com',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '120',  # 内容长度，不用加也可以自动算出来，要是错了会报错
    # 'Accept': '*/*',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',  # 压缩类型，浏览器会解压缩，但是这里不需要压缩，所以不需要这行
    # 'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cookie': 'BAIDUID=B22DE92B9765FF9075E6467A661774EB:FG=1; pgv_pvi=32703488; BIDUPSID=B22DE92B9765FF9075E6467A661774EB; PSTM=1567072215; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=e876838e96daf5121ba3d3a84d91f6cc5eb1690f_1567156261_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; H_PS_PSSID=1464_21091_29522_29521_29721_29568_29221_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1567156259,1567190023; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567190023; __yjsv5_shitong=1.0_7_08da7647f6cb40a2871b363341032068a494_300_1567190095344_81.159.20.255_af4443db',
}
# 处理post表单数据，并变成字节类型（原先是字符串类型）
form_data = urllib.parse.urlencode(form_data).encode()
# 构建请求对象“request”
request = urllib.request.Request(url=post_url, headers=headers)
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())
