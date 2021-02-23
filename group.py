import re
s=input()
x=re.search(r"1{1}1+",s)
print(x.group())
