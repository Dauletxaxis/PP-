import re
s=input()
x=re.findall("[^aeuio][aeiou][aeuio]+[^aeuio]",s)
print(x)
