import random
ran=random.int(1,10)#5
chances=3
while True:
    guess=int(input('enter the number'))
    if guess==ran:
        print('congrats')
        break
    else:
        chances-=1
        continue
if chances<1:
        print('failed try next time')
