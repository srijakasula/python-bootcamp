s='a1b2c3d492nm45'
digits=''
letters=''
for i in s:
    if s.isdigit():
        digits+=i
    if s.ischar():
        letters+=i  
print(letters+digits)        

