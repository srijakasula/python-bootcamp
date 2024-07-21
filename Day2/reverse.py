#reversing the element only int the even position:
mobiles=['iphone','samsung','vivo','oppo','redmi']
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])
