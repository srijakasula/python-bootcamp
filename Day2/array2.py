#print 4,5 as first part and print 1,2,3 as second part
arr=[1,2,3,4,5]
k=2
#5,4,1,2,3
first=arr[k+2:k:-1]
second=arr[:k+1]
print(first+second)
