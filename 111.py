import json

data = {
	"statusCode": 200,
	"data": {
		"totoal": "5",
		"height": "5.97",
		"weight": "10.30",
		"age": "11"
	},
	"msg": "成功"
}

#dumps:把字典转换为json字符串
s = json.dumps(data)
print(s)

#loads:把json转换为dict
s1 = json.loads(s)
print(s1)
