import re

string = '<p><div><span>猪八戒</span></div></p>'
pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')   # 前面的r表示不转译，影响\1和\2

ret = pattern.search(string)
print(ret)
