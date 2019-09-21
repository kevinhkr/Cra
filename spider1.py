import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# with open('baidu.html','w',encoding='utf8') as jj:
#     jj.write(response.read().decode())

# same as:
# with open('baidu.html','wb') as jj:
#     jj.write(response.read())
# wb: write in binary code

# print(dict(response.getheaders()))

print(response.readlines())

# person = {
#     'name': '',
#     'id': 0,
# }
# team = []
#
# for i in range(3):
#     x = person
#     x['id'] = i
#     team.append(x)
#     print(i)
#     print(team)
#
# team[0]['name'] = 'Jack'
# team[1]['name'] = 'Pony'
# team[2]['name'] = 'Joe'
# print(team)
