#print reverse of given string      
def check(s):
    s=s.split()
    rev=' '
    for i in s:
        rev=rev+i[::-1]
    print(type(rev))
    return rev
s='sridevi womens engineering college'
print(check(s))

