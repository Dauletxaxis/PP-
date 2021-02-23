import re
s=input()
x=re.split("[,.]",s)
for i in x:
    print(i)
