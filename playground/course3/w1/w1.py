import re

text = 'loremc-=a+10ipsuma-=adb+=10olorsitamet.'

print(re.findall(r'[abc][+|-]=[abc]|\d+', text))
#print(re.sub(r'(\w)\1', lambda x: x.group(0).upper(), text))
#print(re.sub(r"\b(\w*(\w)\2\w*\b)", r'[\1]', text))