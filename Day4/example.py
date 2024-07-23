s=7
t=11
a=3
b=15
apple=[6,5,-4]
oranges=[9,8,-4]
apple_count=0
orange_count=0
for i in apple:
    if a+i in range(s,t+1):
        apple_count+=1
for i in oranges:
    if b+i in range(s,t+1):
        orange_count+=1
print(apple_count,orange_count)                