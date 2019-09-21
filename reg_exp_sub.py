import re

string = 'i love you, you love me'
pattern = re.compile(r'love')

ret = re.sub(pattern, 'hate', string)
ret1 = pattern.sub('hate', string)
# 两种方法一样
print(ret)
print(ret1)

# 目标：将string1中的身高替换为身高-10
# 例：string1 = '我喜欢身高为170的女生'
# 结果：我喜欢身高为160的女生
string1 = '我喜欢身高为170的女生'


def fn(a):
    b = int(a.group()) - 10
    return str(b)


pattern = re.compile(r'\d+')
ret2 = pattern.sub(fn, string1)
# ret2 = pattern.findall(string1)

print(ret2)
