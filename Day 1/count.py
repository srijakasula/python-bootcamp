#count the digits

s=input()

count=0
for i  in range(0,len(s)):
    if s[i].isdigit():
        count+=1
print(count)
