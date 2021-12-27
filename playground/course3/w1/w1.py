import re

#text = """loremc-=a+10ipsuma-=adb+=10olorsitameta=1cdma=b+100.' \
text = """	a=1 b=2 c=3
    a=+1
    a=-1
    a=b
    a=b+100
    a=b-100"""

d = {'a': 1, 'b': 2, 'c': 3}

matches = re.findall(r"([abc])([-+]?=)([abc]|[-+]?\d+)([-+]?\d+)?", text)  # Если придумать хорошую регулярку, будет просто
for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
	# Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
	#data[v1] = data.get(v2, 0) + int(n or 0)
	print(v1, s, v2, n)

