import re
s=input()
for i in range(1,10):
    b=str(i)
    n=re.search(f"{b}{b}+",s)
    if n!=None:
        print(i)
    else:
        pass

