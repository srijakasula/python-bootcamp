n=101011
s=str(n)
bin=0
j=0
for i in s[::-1]:
    bin+=int(i)*2**j
    j+=1
print(bin)

