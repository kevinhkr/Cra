import re

string = '<div>蛤蛤蛤</div></div></div>'
pattern = re.compile(r'<\w+>.*</\w+>')   # 贪婪，匹配所有
result = pattern.search(string)
print(result)

pattern1 = re.compile(r'<\w+>.*?</\w+>')   # 非贪婪，只匹配一个
result1 = pattern1.search(string)
print(result1)
