cong={7:5,18:22,32:8,71:5,66:6}
bjp={7:15,18:20,32:4,71:9,66:2}
sum1=0
sum2=0
for k,v in cong.items():
    if(k>=18):
        sum1+=v
for k,v in bjp.items():
    if(k>=18):
        sum2+=v
if(sum1>sum2):
    print('majority is cong')
else:
    print('majority bjp')
