# magical or not
n=int(input("enter num:"))
sum=0
while n>0:
    sum+=n%10
    n=n//10
    pro=pro*sum
print(pro)        
