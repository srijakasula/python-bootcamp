#palindrome using for,if

s='python'
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]

if(s1==s):
    print("palindrome") 
else:
    print("not palindrome")   