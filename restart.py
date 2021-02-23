import re
x=int(input())
s=str()
l=[]
for i in range(0,x):
    s=input()
    l.append(s)
for g in l:
    n=re.search("[A-Z]+\s+<{1}[A-Za-z0-9_]+@gmail.com>",g)
    if n!=None:
        print(n.group())
    else:
        pass
    
    
    
    
