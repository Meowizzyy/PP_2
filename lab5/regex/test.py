import re
f = open(r'C:\Users\ruste\Desktop\cxc\lab5\regex\row.txt', 'r', encoding='utf-8')
date = f.read()
x=re.findall("o.?П", date) # работает
print(x)
