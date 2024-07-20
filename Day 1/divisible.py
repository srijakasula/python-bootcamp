#print the count of the numbers divisible by both 4 and 6

def check(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
    return count
arr=[1,36,9,24,4,2,12]
print('the count is:',check(arr)) 
