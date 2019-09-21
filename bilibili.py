import urllib.request
import urllib.parse

url = 'https://www.weibo.com/1897379743/profile?topnav=1&wvr=6&is_all=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': 'login_sid_t=959e29577e245edbf98802e5b2d2c303; cross_origin_proto=SSL; '
              'Ugrow-G0=d52660735d1ea4ed313e0beb68c05fc5; WBStorage=f54cf4e4362237da|undefined; '
              'YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=www.google.com; UOR=www.google.com,www.weibo.com,'
              'www.google.com; Apache=3139000753094.8936.1567507036340; SINAGLOBAL=3139000753094.8936.1567507036340; '
              'ULV=1567507036360:1:1:1:3139000753094.8936.1567507036340:; '
              'SCF=Am7R9YZ26c_QKGGSlG64x6pMqA7iySZqOsEGpdAFdvp0L7zNIH2WZyTZxkJrR_LU-C2Q2mhTsZPh7W46rUgI4OM.; '
              'SUB=_2A25wajIiDeRhGedG4lUS9yfLzz-IHXVTHiTqrDV8PUNbmtBeLVrhkW9NUObKRongZTOwJVkNQbLeyo6iq2tJuIxi; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF1lbHeXWR3TY1Q2Dq830H85JpX5K2hUgL.Fo2R1KM0S0'
              '.NShe2dJLoI77_HsHoIs4DqcvjdNzt; SUHB=0d4_Aw7Lzc4SAa; ALF=1599043050; SSOLoginState=1567507058; '
              'un=13028867249; wvr=6; wb_view_log_1897379743=1920*10801; '
              'YF-Page-G0=112e41ab9e0875e1b6850404cae8fa0e|1567507087|1567507077; '
              'webim_unReadCount=%7B%22time%22%3A1567507091390%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0'
              '%2C%22allcountNum%22%3A37%2C%22msgbox%22%3A0%7D',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

with open('sina.html', 'wb') as fp:
    fp.write(response.read())
