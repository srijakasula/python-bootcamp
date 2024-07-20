#no of consonants in a given string

s='srija'
vowels='aeiouAEIOU'
count=0
for c in s:
    if c not in vowels:
        print(c)
        count+=1
print(count)       
