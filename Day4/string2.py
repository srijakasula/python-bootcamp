s='1C0C1C1A0B1'
res=int(s[0])
for i in range(1,len(s),2):
    if i=='A':
        res=res&int(s[i+1])
    elif i=='B':
        res=res|int(s[i+1])
    elif i=='C':
        res=res^int(s[i+1])
print(res)
